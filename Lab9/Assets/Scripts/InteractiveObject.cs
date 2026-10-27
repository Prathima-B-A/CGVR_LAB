
using UnityEngine;

public class InteractiveObject : MonoBehaviour
{
    public float moveSpeed = 3f;
    public float rotateSpeed = 90f;
    public float scaleSpeed = 1f;

    private Vector3 startPosition;
    private Vector3 startScale;
    private Quaternion startRotation;

    void Start()
    {
        startPosition = transform.position;
        startScale = transform.localScale;
        startRotation = transform.rotation;
    }

    void Update()
    {
        // 1. Translation: arrow keys
        float x = 0f;
        float z = 0f;

        if (Input.GetKey(KeyCode.LeftArrow)) x = -1f;
        if (Input.GetKey(KeyCode.RightArrow)) x = 1f;
        if (Input.GetKey(KeyCode.UpArrow)) z = 1f;
        if (Input.GetKey(KeyCode.DownArrow)) z = -1f;

        transform.position +=
            new Vector3(x, 0f, z) * moveSpeed * Time.deltaTime;

        // 2. Rotation: Q and E
        if (Input.GetKey(KeyCode.Q))
            transform.Rotate(Vector3.up,
                -rotateSpeed * Time.deltaTime);

        if (Input.GetKey(KeyCode.E))
            transform.Rotate(Vector3.up,
                rotateSpeed * Time.deltaTime);

        // 3. Scaling: + and -
        if (Input.GetKey(KeyCode.Equals) ||
            Input.GetKey(KeyCode.KeypadPlus))
        {
            transform.localScale +=
                Vector3.one * scaleSpeed * Time.deltaTime;
        }

        if (Input.GetKey(KeyCode.Minus) ||
            Input.GetKey(KeyCode.KeypadMinus))
        {
            transform.localScale = Vector3.Max(
                Vector3.one * 0.2f,
                transform.localScale -
                Vector3.one * scaleSpeed * Time.deltaTime);
        }

        // 4. Reset the object: R
        if (Input.GetKeyDown(KeyCode.R))
        {
            transform.position = startPosition;
            transform.localScale = startScale;
            transform.rotation = startRotation;
        }
    }
}
