# devops-pre-test


Arsitektur Tingkat Tinggi pada GCP:
Google Kubernetes Engine (GKE):

Gunakan Kubernetes Engine di Google Cloud untuk menampung aplikasi dalam wadah (container).
GKE dapat digunakan untuk melakukan orkestrasi aplikasi yang di-dockerize menggunakan Kubernetes.
Google Container Registry (GCR):

Simpan Docker image yang telah Anda buat (pada poin 2) di Google Container Registry.
GCR adalah registry docker bawaan dari Google Cloud Platform yang memungkinkan penyimpanan aman untuk image Docker.
Networking:

Anda perlu menyesuaikan layanan GKE dan mengatur networking di GCP.
Pastikan untuk menyesuaikan jaringan antara layanan GKE, GCR, dan aplikasi yang akan di-host.
Additional Services:

Untuk deployment aplikasi ke Google Cloud, Anda mungkin membutuhkan layanan yang lain tergantung pada aplikasi Anda.
Misalnya, Cloud Load Balancer, Cloud DNS, atau layanan lain yang dibutuhkan untuk aplikasi dan pengaturan infrastruktur.
Security & IAM:

Penting untuk mengatur keamanan, izin akses, dan manajemen identitas (IAM) untuk semua layanan yang Anda gunakan di GCP.
