/* static/js/interactions.js */

document.addEventListener('DOMContentLoaded', function() {

    // --- 1. Status Pill Colorizer ---
    // Automatically adds the correct class based on the text inside the pill
    const pills = document.querySelectorAll('.status-pill');
    pills.forEach(pill => {
        const status = pill.innerText.trim().toLowerCase();
        if (status === 'delivered') {
            pill.classList.add('status-delivered');
        } else if (status === 'pending') {
            pill.classList.add('status-pending');
        } else if (status === 'out for delivery') {
            pill.classList.add('status-out-for-delivery');
        } else {
            pill.style.background = 'rgba(255,255,255,0.1)';
        }
    });

    // --- 2. Sparklines Configuration ---
    const commonOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: { legend: { display: false }, tooltip: { enabled: false } },
        scales: {
            x: { display: false },
            y: { display: false }
        },
        elements: {
            point: { radius: 0 },
            line: { tension: 0.4, borderWidth: 2 }
        }
    };

    function createGradient(ctx, color) {
        const gradient = ctx.createLinearGradient(0, 0, 0, 60);
        gradient.addColorStop(0, color.replace(')', ', 0.4)').replace('rgb', 'rgba'));
        gradient.addColorStop(1, color.replace(')', ', 0.0)').replace('rgb', 'rgba'));
        return gradient;
    }

    // Chart 1: Total (Purple)
    const ctx1 = document.getElementById('sparkTotal');
    if (ctx1) {
        new Chart(ctx1.getContext('2d'), {
            type: 'line',
            data: {
                labels: [1, 2, 3, 4, 5, 6],
                datasets: [{
                    data: [10, 15, 12, 18, 20, 24],
                    borderColor: '#A855F7',
                    backgroundColor: createGradient(ctx1.getContext('2d'), 'rgb(168, 85, 247)'),
                    fill: true
                }]
            },
            options: commonOptions
        });
    }

    // Chart 2: Delivered (Green)
    const ctx2 = document.getElementById('sparkDelivered');
    if (ctx2) {
        new Chart(ctx2.getContext('2d'), {
            type: 'line',
            data: {
                labels: [1, 2, 3, 4, 5, 6],
                datasets: [{
                    data: [5, 8, 7, 12, 15, 18],
                    borderColor: '#22C55E',
                    backgroundColor: createGradient(ctx2.getContext('2d'), 'rgb(34, 197, 94)'),
                    fill: true
                }]
            },
            options: commonOptions
        });
    }

    // Chart 3: Pending (Orange)
    const ctx3 = document.getElementById('sparkPending');
    if (ctx3) {
        new Chart(ctx3.getContext('2d'), {
            type: 'line',
            data: {
                labels: [1, 2, 3, 4, 5, 6],
                datasets: [{
                    data: [8, 6, 9, 5, 4, 3],
                    borderColor: '#F97316',
                    backgroundColor: createGradient(ctx3.getContext('2d'), 'rgb(249, 115, 22)'),
                    fill: true
                }]
            },
            options: commonOptions
        });
    }
});