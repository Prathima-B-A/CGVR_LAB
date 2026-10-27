Shader "Custom/Transform2D"
{
    Properties { _Color("Color", Color) = (1, 0.5, 0, 1) }
    SubShader
    {
        Tags { "RenderType"="Opaque" "RenderPipeline"="UniversalPipeline" }
        Pass
        {
            Cull Off
            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"

            float4x4 _TransformMatrix;
            CBUFFER_START(UnityPerMaterial)
                half4 _Color;
            CBUFFER_END

            struct Attributes { float4 positionOS : POSITION; };
            struct Varyings   { float4 positionCS : SV_POSITION; };

            // Vertex shader: applies the homogeneous transformation matrix
            Varyings vert(Attributes IN)
            {
                Varyings OUT;
                float4 p = mul(_TransformMatrix, float4(IN.positionOS.xy, 0, 1));
                OUT.positionCS = TransformObjectToHClip(p.xyz);
                return OUT;
            }

            // Fragment shader: colors each pixel
            half4 frag(Varyings IN) : SV_Target
            {
                return _Color;
            }
            ENDHLSL
        }
    }
}