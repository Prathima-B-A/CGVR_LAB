using UnityEngine;

public class ViewingPipeline : MonoBehaviour
{
    [Header("Object (Model) Transform")]
    public Vector3 objPosition = new Vector3(0, 0, 0);
    public Vector3 objRotation = new Vector3(20, 30, 0);
    public Vector3 objScale = new Vector3(1, 1, 1);
    public bool autoRotate = true;

    [Header("Camera (View) Transform")]
    public Vector3 camPosition = new Vector3(0, 0, -5);
    public Vector3 camRotation = new Vector3(0, 0, 0);

    [Header("Projection")]
    public bool perspective = true;
    public float fov = 60f;
    public float nearPlane = 0.3f;
    public float farPlane = 50f;
    public float orthoSize = 2.5f;

    [Header("Viewport (pixels, origin bottom-left)")]
    public float vpX = 100;
    public float vpY = 100;
    public float vpW = 500;
    public float vpH = 400;

    // 8 corners of a cube in LOCAL space
    Vector3[] verts = {
        new Vector3(-1,-1,-1), new Vector3( 1,-1,-1),
        new Vector3( 1, 1,-1), new Vector3(-1, 1,-1),
        new Vector3(-1,-1, 1), new Vector3( 1,-1, 1),
        new Vector3( 1, 1, 1), new Vector3(-1, 1, 1)
    };

    // 12 edges as pairs of vertex indices
    int[,] edges = {
        {0,1},{1,2},{2,3},{3,0},
        {4,5},{5,6},{6,7},{7,4},
        {0,4},{1,5},{2,6},{3,7}
    };

    void Update()
    {
        if (autoRotate) objRotation.y += 30f * Time.deltaTime;
    }

    void OnGUI()
    {
        // 1. MODEL matrix: local -> world
        Matrix4x4 M = Matrix4x4.TRS(objPosition,
                                    Quaternion.Euler(objRotation),
                                    objScale);

        // 2. VIEW matrix: world -> camera space
        Matrix4x4 camToWorld = Matrix4x4.TRS(camPosition,
                                             Quaternion.Euler(camRotation),
                                             Vector3.one);
        Matrix4x4 V = Matrix4x4.Scale(new Vector3(1, 1, -1)) * camToWorld.inverse;

        // 3. PROJECTION matrix: camera -> clip space
        float aspect = vpW / vpH;
        Matrix4x4 P;
        if (perspective)
            P = Matrix4x4.Perspective(fov, aspect, nearPlane, farPlane);
        else
            P = Matrix4x4.Ortho(-orthoSize * aspect, orthoSize * aspect,
                                -orthoSize, orthoSize, nearPlane, farPlane);

        Matrix4x4 MVP = P * V * M;

        Vector2[] screen = new Vector2[verts.Length];
        bool[] visible = new bool[verts.Length];

        for (int i = 0; i < verts.Length; i++)
        {
            Vector4 v = new Vector4(verts[i].x, verts[i].y, verts[i].z, 1f);
            Vector4 clip = MVP * v;

            if (clip.w <= 0.0001f) { visible[i] = false; continue; }

            // 4. PERSPECTIVE DIVIDE -> NDC
            float ndcX = clip.x / clip.w;
            float ndcY = clip.y / clip.w;

            // 5. VIEWPORT MAPPING -> pixels
            float sx = vpX + (ndcX + 1f) * 0.5f * vpW;
            float sy = vpY + (ndcY + 1f) * 0.5f * vpH;

            screen[i] = new Vector2(sx, Screen.height - sy);
            visible[i] = true;
        }

        // Viewport border
        GUI.color = Color.gray;
        Rect border = new Rect(vpX, Screen.height - vpY - vpH, vpW, vpH);
        DrawRectOutline(border, 2);

        // Cube edges
        GUI.color = Color.green;
        for (int e = 0; e < edges.GetLength(0); e++)
        {
            int a = edges[e, 0], b = edges[e, 1];
            if (visible[a] && visible[b])
                DrawLine(screen[a], screen[b], 2f);
        }

        // Labels and button
        GUI.color = Color.white;
        GUI.Label(new Rect(10, 10, 500, 25),
            "Projection: " + (perspective ? "Perspective" : "Orthographic"));
        if (GUI.Button(new Rect(10, 40, 160, 30), "Toggle Projection"))
            perspective = !perspective;
    }

    static void DrawLine(Vector2 a, Vector2 b, float width)
    {
        Matrix4x4 saved = GUI.matrix;
        float angle = Mathf.Atan2(b.y - a.y, b.x - a.x) * Mathf.Rad2Deg;
        float len = (b - a).magnitude;
        GUIUtility.RotateAroundPivot(angle, a);
        GUI.DrawTexture(new Rect(a.x, a.y - width / 2f, len, width),
                        Texture2D.whiteTexture);
        GUI.matrix = saved;
    }

    static void DrawRectOutline(Rect r, float t)
    {
        GUI.DrawTexture(new Rect(r.x, r.y, r.width, t), Texture2D.whiteTexture);
        GUI.DrawTexture(new Rect(r.x, r.yMax - t, r.width, t), Texture2D.whiteTexture);
        GUI.DrawTexture(new Rect(r.x, r.y, t, r.height), Texture2D.whiteTexture);
        GUI.DrawTexture(new Rect(r.xMax - t, r.y, t, r.height), Texture2D.whiteTexture);
    }
}