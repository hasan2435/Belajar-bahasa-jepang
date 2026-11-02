#!/usr/bin/env python3
"""
Belajar Bahasa Jepang - versi terminal, bisa dijalankan sendiri.
  python3 belajar_jepang.py
Menu: tabel Hiragana/Katakana, kuis kana, kosakata N5, tata bahasa dasar N5.
Ini versi terminal ringkas dari aplikasi web (22 tahap). Materi di bawah
adalah materi dasar standar, bukan seluruh isi aplikasi web.
"""
import random

HIRAGANA = [("あ","a"),("い","i"),("う","u"),("え","e"),("お","o"),
 ("か","ka"),("き","ki"),("く","ku"),("け","ke"),("こ","ko"),
 ("さ","sa"),("し","shi"),("す","su"),("せ","se"),("そ","so"),
 ("た","ta"),("ち","chi"),("つ","tsu"),("て","te"),("と","to"),
 ("な","na"),("に","ni"),("ぬ","nu"),("ね","ne"),("の","no"),
 ("は","ha"),("ひ","hi"),("ふ","fu"),("へ","he"),("ほ","ho"),
 ("ま","ma"),("み","mi"),("む","mu"),("め","me"),("も","mo"),
 ("や","ya"),("ゆ","yu"),("よ","yo"),
 ("ら","ra"),("り","ri"),("る","ru"),("れ","re"),("ろ","ro"),
 ("わ","wa"),("を","wo"),("ん","n")]
KATAKANA = [("ア","a"),("イ","i"),("ウ","u"),("エ","e"),("オ","o"),
 ("カ","ka"),("キ","ki"),("ク","ku"),("ケ","ke"),("コ","ko"),
 ("サ","sa"),("シ","shi"),("ス","su"),("セ","se"),("ソ","so"),
 ("タ","ta"),("チ","chi"),("ツ","tsu"),("テ","te"),("ト","to"),
 ("ナ","na"),("ニ","ni"),("ヌ","nu"),("ネ","ne"),("ノ","no"),
 ("ハ","ha"),("ヒ","hi"),("フ","fu"),("ヘ","he"),("ホ","ho"),
 ("マ","ma"),("ミ","mi"),("ム","mu"),("メ","me"),("モ","mo"),
 ("ヤ","ya"),("ユ","yu"),("ヨ","yo"),
 ("ラ","ra"),("リ","ri"),("ル","ru"),("レ","re"),("ロ","ro"),
 ("ワ","wa"),("ヲ","wo"),("ン","n")]
KOSAKATA_N5 = [
 ("水","みず","mizu","air"),("火","ひ","hi","api"),("山","やま","yama","gunung"),
 ("川","かわ","kawa","sungai"),("空","そら","sora","langit"),("雨","あめ","ame","hujan"),
 ("学校","がっこう","gakkou","sekolah"),("先生","せんせい","sensei","guru"),
 ("友達","ともだち","tomodachi","teman"),("家族","かぞく","kazoku","keluarga"),
 ("食べる","たべる","taberu","makan"),("飲む","のむ","nomu","minum"),
 ("行く","いく","iku","pergi"),("来る","くる","kuru","datang"),("見る","みる","miru","melihat"),
 ("大きい","おおきい","ookii","besar"),("小さい","ちいさい","chiisai","kecil"),
 ("新しい","あたらしい","atarashii","baru"),("古い","ふるい","furui","tua/lama"),
 ("今日","きょう","kyou","hari ini"),("明日","あした","ashita","besok"),
]
TATA_BAHASA = [
 ("X は Y です","X wa Y desu","X adalah Y. Contoh: 私は学生です (Watashi wa gakusei desu) = Saya adalah murid."),
 ("X を Y ます","X wo Y-masu","Melakukan Y terhadap X. Contoh: 本を読みます (Hon wo yomimasu) = Membaca buku."),
 ("X に 行きます","X ni ikimasu","Pergi ke X. Contoh: 学校に行きます (Gakkou ni ikimasu) = Pergi ke sekolah."),
]

def tabel(data, judul):
    print(f"\n=== {judul} ===")
    for i in range(0, len(data), 5):
        print("  ".join(f"{k}={r}" for k, r in data[i:i+5]))

def kuis(data, judul):
    print(f"\n=== Kuis {judul} (ketik romaji, kosongkan untuk berhenti) ===")
    soal = random.sample(data, 10); benar = 0
    for k, r in soal:
        j = input(f"{k} = ").strip().lower()
        if not j: break
        if j == r: print("  Benar!"); benar += 1
        else: print(f"  Salah, jawabannya {r}")
    print(f"Skor: {benar}/10")

def main():
    while True:
        print("\nMenu: 1=Tabel Hiragana  2=Tabel Katakana  3=Kuis Hiragana  4=Kuis Katakana  5=Kosakata N5  6=Tata Bahasa N5  0=Keluar")
        p = input("Pilih: ").strip()
        if p == "0": break
        elif p == "1": tabel(HIRAGANA, "Hiragana")
        elif p == "2": tabel(KATAKANA, "Katakana")
        elif p == "3": kuis(HIRAGANA, "Hiragana")
        elif p == "4": kuis(KATAKANA, "Katakana")
        elif p == "5":
            print("\n=== Kosakata N5 ===")
            for kanji, kana, romaji, arti in KOSAKATA_N5: print(f"{kanji} {kana} ({romaji}) = {arti}")
        elif p == "6":
            print("\n=== Tata Bahasa N5 ===")
            for pola, romaji, penjelas in TATA_BAHASA: print(f"{pola} ({romaji}) — {penjelas}")
        else: print("Pilihan tidak dikenal.")

if __name__ == "__main__":
    main()
