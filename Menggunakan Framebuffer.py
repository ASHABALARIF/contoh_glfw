import glfw
from OpenGL.GL import *

# ... (kode inisialisasi jendela) ...

framebuffer = glGenFramebuffers(1)
glBindFramebuffer(GL_FRAMEBUFFER, framebuffer)

# ... (membuat tekstur untuk framebuffer) ...

glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, texture, 0)

# ... (loop utama) ...