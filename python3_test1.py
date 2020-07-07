class MP3Player:
    def play_music(self):
        print('音楽を再生します')

    def next_song(self):
        print('次の曲を再生します')

    def previous_song(self):
        print('前の曲を再生します')

    def stop_music(self):
        print('音楽を止めます')

mp = MP3Player()
mp.play_music()
mp.next_song()
mp.previous_song()
mp.stop_music()

class CellPhone:
    def __init__(self, tel_numer, mail_address):
        self.tel_numer = tel_numer
        self.mail_address = mail_address

    def call(self):
        print(self.tel_numer,'から発信します')

    def send_mail(self):
        print(self.mail_address,'から送信します')

cp = CellPhone('08000000000','aaa@gmail.com')
cp.call()
cp.send_mail()

class SmartPhone(MP3Player, CellPhone):
    def call(self):
        super().call()

    def send_mail(self):
        super().send_mail()

sp = SmartPhone('08000000000','aaa@gmail.com')
sp.play_music()
sp.next_song()
sp.previous_song()
sp.stop_music()
sp.call()
sp.send_mail()