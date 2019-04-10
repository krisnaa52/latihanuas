class Person():
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.__umur = 0

    def toString(self):
        return "nama : {} , Alamat : {} : umur : {}" \
            .format(self.nama, self.alamat, self.__umur)

    def ubahUmur(self, umur):
        self.__umur = umur

    @property
    def umur(self):
        return "umurnya {} adalah {} ".format(self.nama, self.umur)
