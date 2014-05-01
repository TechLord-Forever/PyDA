from settings import *
# import traceback

class Disassembler:
    def load(self, binary):
        self.binary = binary
        for format in IMPORTED_FORMATS:
            try:
                self.dis = format.disassemble(self.binary)
                break
            except:
                # traceback.print_exc()
                print "Nope, not",`format`
        if not self.dis:
            raise UnsupportedBinaryFormatException()

    def getFileType(self):
        return self.dis.FILETYPE_NAME

    def disassemble(self):
        return self.dis.disassemble()

class UnsupportedBinaryFormatException(Exception):
    pass
