import glfw
from OpenGL.GL import *

# ... (kode inisialisasi jendela) ...

vertex_shader = """
#version 330 core
layout (location = 0) in vec3 aPos;
void main()
{
    gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
}
"""

fragment_shader = """
#version 330 core
out vec4 FragColor;
void main()
{
    FragColor = vec4(1.0, 0.5, 0.2, 1.0);
}
"""

# ... (kompilasi dan penggunaan shader) ...

# ... (loop utama) ...