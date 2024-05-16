document.addEventListener('DOMContentLoaded', function() {
    // Menampilkan pesan "File terpilih" ketika pengguna memilih gambar
    const fileInput = document.querySelector('input[type="file"]');
    const resultDiv = document.getElementById('result');

    fileInput.addEventListener('change', function() {
        const fileName = fileInput.files[0].name;
        resultDiv.innerHTML = `<h2>File Terpilih:</h2><p>${fileName}</p>`;
    });

    // Menghapus hasil OCR saat pengguna mengklik tombol "Hapus"
    const clearButton = document.getElementById('clear-button');
    clearButton.addEventListener('click', function() {
        resultDiv.innerHTML = '<h2>Hasil OCR:</h2><p></p>';
    });
});
