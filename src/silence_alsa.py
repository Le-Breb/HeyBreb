import ctypes

c_error_handler = None

def silence_alsa():
    global c_error_handler
    try:
        asound = ctypes.cdll.LoadLibrary('libasound.so')
        # Define a callback type: int handler(const char *file, int line, const char *function, int err, const char *fmt, ...)
        ERROR_HANDLER_FUNC = ctypes.CFUNCTYPE(
            None,
            ctypes.c_char_p,
            ctypes.c_int,
            ctypes.c_char_p,
            ctypes.c_int,
            ctypes.c_char_p
        )

        def py_error_handler(filename, line, function, err, fmt):
            # do nothing → silences ALSA
            return

        c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
        asound.snd_lib_error_set_handler(c_error_handler)
    except OSError:
        pass
