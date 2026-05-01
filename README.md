# 📌 Dijkstra algoritmi (Python)

## 📖 Tavsif

Ushbu loyiha Python dasturlash tilida **Dijkstra algoritmi** yordamida og‘irlikli grafdagi eng qisqa yo‘llarni topishni ko‘rsatadi.

Bu algoritm quyidagi sohalarda keng qo‘llaniladi:

* GPS va navigatsiya tizimlari
* Tarmoq marshrutlash
* Yo‘l topish (pathfinding) masalalari

---

## ⚙️ Qanday ishlaydi

Dijkstra algoritmi **greedy (ochko‘z)** yondashuv asosida ishlaydi:

1. Boshlang‘ich tugunni tanlaydi
2. Qo‘shni tugunlar uchun eng qisqa masofalarni hisoblaydi
3. Har doim eng kichik masofali tugunni tanlaydi
4. Barcha tugunlar ko‘rib chiqilgunga qadar davom etadi

---

## 🧠 Algoritm xususiyatlari

* **Priority Queue (heapq)** ishlatiladi
* Murakkablik: **O((V + E) log V)**
* Faqat **manfiy bo‘lmagan og‘irliklar** bilan ishlaydi

---

## 📂 Graf tuzilishi

Graf adjacency list (qo‘shnichilik ro‘yxati) ko‘rinishida beriladi:

```python id="k29x7v"
graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('A', 5), ('C', 2), ('D', 1)],
    'C': [('A', 1), ('B', 2), ('D', 4), ('E', 8)],
    'D': [('B', 1), ('C', 4), ('E', 3), ('F', 6)],
    'E': [('C', 8), ('D', 3)],
    'F': [('D', 6)]
}
```

---

## 🚀 Ishga tushirish

Dastur faylini ishga tushiring:

```bash id="n12jdp"
python dijkstra.py
```

---

## ✅ Namuna natija

```id="q81kdm"
A -> A = 0
A -> B = 3
A -> C = 1
A -> D = 4
A -> E = 7
A -> F = 10
```

---

## ⚠️ Cheklovlar

* **Manfiy og‘irliklar** bilan ishlamaydi
* Bunday holatda **Bellman-Ford algoritmi** ishlatiladi

---

## 📌 Talablar

* Python 3.x
* Standart kutubxona: `heapq`

---

## 👨‍💻 Muallif

Ushbu loyiha Python’da graf algoritmlarini o‘rganish uchun yaratilgan.

---
