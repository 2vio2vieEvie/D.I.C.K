# D.I.C.K.
Generally intended to be used in situations where NVIDIA's exported DDS have a signature (which can be viewed in hex) that may end up breaking certain software from being able to read the format.

This tool will null those hexadecimal blocks in order to get rid of the signature, allowing for clearer reading of the dds compression used as well as the texture itself.


Very specific form of usage, haven't really come across any cases where doing this may be necessary but you never know when this may come in handy.
