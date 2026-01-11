// 1. Başa Dön Oku Mantığı
const topBtn = document.getElementById("backToTop");

window.onscroll = function() {
    // Sayfa 300px'den fazla aşağı kaydırıldığında butonu göster
    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
        topBtn.style.display = "flex";
    } else {
        topBtn.style.display = "none";
    }
};

topBtn.onclick = function() {
    // Yumuşak bir şekilde sayfanın en üstüne kaydır
    window.scrollTo({ top: 0, behavior: 'smooth' });
};

// 2. Navigasyon Linkleri için Yumuşak Kaydırma (Smooth Scroll)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault(); // Varsayılan tıklama davranışını engelle

        const targetId = this.getAttribute('href');
        const targetElement = document.querySelector(targetId);

        if (targetElement) {
            // Hedef elementin pozisyonunu al ve navbar yüksekliğini çıkar
            const navbarHeight = document.getElementById('navbar').offsetHeight;
            const targetPosition = targetElement.getBoundingClientRect().top + window.pageYOffset - navbarHeight;

            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        }
    });
});
