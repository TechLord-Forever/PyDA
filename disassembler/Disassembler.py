from settings import *
# import traceback

class Disassembler:
    def __init__(self, settings_manager):
        self.settings_manager = settings_manager

    def load(self, binary, filename = None):
        self.binary = binary
        for format in IMPORTED_FORMATS:
            try:
                self.dis = format.disassemble(self.binary, filename=filename)
                break
            except:
                print 'File header did not match %s' % format.FILETYPE_NAME
                # traceback.print_exc()

        if not self.dis:
            raise UnsupportedBinaryFormatException()

    def getFileType(self):
        return self.dis.FILETYPE_NAME

    def disassemble(self):
        return self.dis.disassemble(self.settings_manager)

class UnsupportedBinaryFormatException(Exception):
    pass
