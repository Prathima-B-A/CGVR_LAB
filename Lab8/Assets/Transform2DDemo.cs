using UnityEngine;

public class Transform2DDemo : MonoBehaviour
{
    public enum Mode { Translation, Rotation, Scaling, ReflectionX, ReflectionY, ShearX, ShearY }
    public Mode mode = Mode.Translation;

    public float tx = 1f, ty = 1f;      // translation
    public float angle = 45f;           // rotation (degrees)
    public float sx = 1.5f, sy = 1.5f;  // scaling
    public float shx = 0.5f, shy = 0.5f;// shearing

    Material mat;

    void Start()
    {
        Mesh m = new Mesh();
        m.vertices = new Vector3[] {
            new Vector3(-0.5f, -0.5f, 0),
            new Vector3( 0.5f, -0.5f, 0),
            new Vector3( 0.0f,  0.5f, 0) };
        m.triangles = new int[] { 0, 2, 1 };

        gameObject.AddComponent<MeshFilter>().mesh = m;
        mat = new Material(Shader.Find("Custom/Transform2D"));
        gameObject.AddComponent<MeshRenderer>().material = mat;
    }

    void Update()
    {
        mat.SetMatrix("_TransformMatrix", GetMatrix());
    }

    // 3x3 homogeneous matrix [a b tx; c d ty; 0 0 1] stored in a 4x4
    Matrix4x4 Make(float a, float b, float c, float d, float x, float y)
    {
        Matrix4x4 M = Matrix4x4.identity;
        M.SetRow(0, new Vector4(a, b, 0, x));
        M.SetRow(1, new Vector4(c, d, 0, y));
        return M;
    }

    Matrix4x4 GetMatrix()
    {
        float r = angle * Mathf.Deg2Rad;
        switch (mode)
        {
            case Mode.Translation: return Make(1, 0, 0, 1, tx, ty);
            case Mode.Rotation: return Make(Mathf.Cos(r), -Mathf.Sin(r), Mathf.Sin(r), Mathf.Cos(r), 0, 0);
            case Mode.Scaling: return Make(sx, 0, 0, sy, 0, 0);
            case Mode.ReflectionX: return Make(1, 0, 0, -1, 0, 0);  // about X-axis
            case Mode.ReflectionY: return Make(-1, 0, 0, 1, 0, 0);  // about Y-axis
            case Mode.ShearX: return Make(1, shx, 0, 1, 0, 0);
            case Mode.ShearY: return Make(1, 0, shy, 1, 0, 0);
        }
        return Matrix4x4.identity;
    }
}