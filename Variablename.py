from itertools import groupby

START = 'q0'                 
FINAL = {'q1'}               
DEAD = 'qdead'               

def klasifikasi(c):
    """Mengubah satu karakter menjadi simbol alfabet DFA."""
    if c.isascii() and c.isalpha():
        return 'huruf'
    if c.isascii() and c.isdigit():
        return 'angka'
    if c == '_':
        return '_'
    return 'lainnya'

DELTA = {
    ('q0', 'huruf'): 'q1',
    ('q0', '_'): 'q1',
    ('q1', 'huruf'): 'q1',
    ('q1', 'angka'): 'q1',
    ('q1', '_'): 'q1',
}

def validasi_variable(teks):
    """Mengembalikan (diterima?, jejak state, posisi karakter penyebab dead state)."""
    state = START
    jejak = [state]
    
    for i, ch in enumerate(teks, start=1):
        state = DELTA.get((state, klasifikasi(ch)), DEAD)
        jejak.append(state)
        if state == DEAD:
            return False, jejak, i
            
    return state in FINAL, jejak, None

def ringkas(jejak):
    """Meringkas jejak, misalnya q1 q1 q1 menjadi 'q1 (x3)'."""
    bagian = []
    for state, grup in groupby(jejak):
        n = len(list(grup))
        bagian.append(state if n == 1 else f'{state} (x{n})')
    return ' -> '.join(bagian)

def tampilkan(teks):
    ok, jejak, pos = validasi_variable(teks)
    print(f'Input : {teks!r}')
    print(f'Jejak : {ringkas(jejak)}')
    if pos:
        print(f'Hasil : TIDAK VALID (ditolak pada karakter ke-{pos}: {teks[pos - 1]!r})')
    else:
        print(f'Hasil : {"VALID" if ok else "TIDAK VALID (string berhenti di state non-akhir)"}')
    print()

if __name__ == '__main__':
    uji = [
        'nama_variabel',
        '_totalHarga',
        'x1',
        '2nama',
        'nama-variabel',
        'nama variabel',
        'user@domain',
        ''
    ]
    
    for s in uji:
        tampilkan(s)
        
    print('--- Mode input (ketik nama variabel, kosongkan untuk berhenti) ---')
    while True:
        teks = input('Masukkan nama variabel: ')
        if teks == '':
            break
        tampilkan(teks)