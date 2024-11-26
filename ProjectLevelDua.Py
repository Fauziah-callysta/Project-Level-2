import heapq

class NavigasiUniversitas:
    def __init__(self):
        # Graf merepresentasikan ruangan dan jarak antar mereka
        self.graph = {
            "Lobi": {"Kelas A": 3, "Kelas B": 2},
            "Kelas A": {"Lobi": 3, "Perpustakaan": 4, "Kantin": 7},
            "Kelas B": {"Lobi": 2, "Perpustakaan": 6},
            "Perpustakaan": {"Kelas A": 4, "Kelas B": 6, "Lab Komputer": 3},
            "Lab Komputer": {"Perpustakaan": 3, "Kantin": 5},
            "Kantin": {"Kelas A": 7, "Lab Komputer": 5},
        }

    def cari_rute_terpendek(self, start, end):
        """Menggunakan algoritma Dijkstra untuk mencari rute terpendek."""
        queue = [(0, start, [])]  # (jarak total, lokasi saat ini, rute yang dilalui)
        visited = set()

        while queue:
            jarak, lokasi, rute = heapq.heappop(queue)

            if lokasi in visited:
                continue

            visited.add(lokasi)
            rute = rute + [lokasi]

            if lokasi == end:
                return rute, jarak

            for tetangga, jarak_tempuh in self.graph.get(lokasi, {}).items():
                if tetangga not in visited:
                    heapq.heappush(queue, (jarak + jarak_tempuh, tetangga, rute))

        return [], float("inf")

def main():
    navigasi = NavigasiUniversitas()

    print("Selamat datang di Sistem Navigasi Universitas!")
    print("Ruangan yang tersedia: Lobi, Kelas A, Kelas B, Perpustakaan, Lab Komputer, Kantin")

    start = input("Masukkan ruangan awal: ").strip().title()
    end = input("Masukkan ruangan tujuan: ").strip().title()

    rute, jarak = navigasi.cari_rute_terpendek(start, end)

    if jarak != float("inf"):
        print(f"Rute terpendek dari {start} ke {end}: {' -> '.join(rute)} (Jarak: {jarak} meter).")
    else:
        print(f"Tidak ada rute dari {start} ke {end}. Silakan coba lagi.")

if __name__ == "__main__":
    main()