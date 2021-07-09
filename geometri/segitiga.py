from geometri.bangunruang import BangunRuang


class SegiTiga(BangunRuang):
    def __init__(self, a, t):
        #fungsi yang pertama kali ketika objek diciptakan
        self.a = a
        self.t = t

    def info(self):
        return f'Ini adalah object dari segi tiga dengan alas={self.a} dan lebar={self.t}'

    def hitung_luas(self):
        return self.a * self.t / 2