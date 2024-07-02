library = [
    {"judul": "LASKAR PELANGI", "pengarang": "ANDREA HIRATA", "tahun": 2005},
    {"judul": "SANG PEMIMPI", "pengarang": "ANDREA HIRATA", "tahun": 2006},
    {"judul": "EDENSOR", "pengarang": "ANDREA HIRATA", "tahun": 2007},
    {"judul": "PADANG BULAN", "pengarang": "ANDREA HIRATA", "tahun": 2010},
    {"judul": "AYAH", "pengarang": "ANDREA HIRATA", "tahun": 2015},
    {"judul": "DEAR NATHAN", "pengarang": "ERISCA FEBRIANI", "tahun": 2015},
    {"judul": "HELLO SALMA", "pengarang": "ERISCA FEBRIANI", "tahun": 2018},
    {"judul": "GOODBYE DANIEL", "pengarang": "ERISCA FEBRIANI", "tahun": 2021},
    {"judul": "KISAH UNTUK GERRY", "pengarang": "ERISCA FEBRIANI", "tahun": 2019},
    {"judul": "KISAH UNTUK DINDA", "pengarang": "ERISCA FEBRIANI", "tahun": 2021},
    {"judul": "CINTA BRONTOSAURUS", "pengarang": "RADITYA DIKA", "tahun": 2006},
    {"judul": "MARMUT MERAH JAMBU", "pengarang": "RADITYA DIKA", "tahun": 2009},
    {"judul": "MANUSIA SETENGAH SALMON", "pengarang": "RADITYA DIKA", "tahun": 2011},
    {"judul": "KOALA KUMAL", "pengarang": "RADITYA DIKA", "tahun": 2015},
    {"judul": "KAMBING JANTAN", "pengarang": "RADITYA DIKA", "tahun": 2009}
]

def display_books(books):
    if books:
        print(f"{'No.':<4} {'Judul':<30} {'Pengarang':<20} {'Tahun':<5}")
        print("-" * 60)
        for i, book in enumerate(books, start=1):
            print(f"{i:<4} {book['judul']:<30} {book['pengarang']:<20} {book['tahun']:<5}")
    else:
        print("TIDAK ADA BUKU YANG DITEMUKKAN.")

def search_book():
    while True:
        print("PILIH OPSI:")
        print("1. LIHAT DAFTAR BUKU")
        print("2. CARI BERDASARKAN JUDUL")
        print("3. CARI BERDASARKAN PENULIS")
        print("4. CARI BERDASARKAN TAHUN")
        print("5. TAMBAH BUKU")
        print("6. HAPUS BUKU")
        print("7. KELUAR")

        choice = input("MASUKKAN PILIHAN: ")
        print("\n")

        if choice == "1":
            display_books(library)
        elif choice == "2":
            title = input("MASUKKAN JUDUL BUKU: ").strip()
            results = [book for book in library if title.lower() in book['judul'].lower()]
            display_books(results)
        elif choice == "3":
            author = input("MASUKKAN NAMA PENULIS: ").strip()
            results = [book for book in library if author.lower() in book['pengarang'].lower()]
            display_books(results)
        elif choice == "4":
            year = input("MASUKKAN TAHUN: ").strip()
            results = [book for book in library if str(year) == str(book['tahun'])]
            display_books(results)
        elif choice == "5":
            new_book = {}
            new_book['judul'] = input("MASUKKAN JUDUL BUKU: ").strip()
            new_book['pengarang'] = input("MASUKKAN NAMA PENULIS: ").strip()
            new_book['tahun'] = input("MASUKKAN TAHUN: ").strip()
            library.append(new_book)
            print("\nBUKU BERHASIL DITAMBAHKAN.")
            display_books(library)
        elif choice == "6":
            display_books(library)
            index = int(input("\nMASUKKAN NOMOR BUKU YANG INGIN DIHAPUS: ")) - 1
            if 0 <= index < len(library):
                removed_book = library.pop(index)
                print(f"\nBUKU '{removed_book['judul']}' BERHASIL DIHAPUS.")
            else:
                print("NOMOR BUKU TIDAK VALID.")
            display_books(library)
        elif choice == "7":
            break
        else:
            print("PILIHAN TIDAK VALID.")

# Call the function to test it
search_book()
