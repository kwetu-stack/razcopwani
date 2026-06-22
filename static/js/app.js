function renderChart(id, type, labels, values) {
  const canvas = document.getElementById(id);
  if (!canvas) return;
  const palette = ['#22d3ee', '#38bdf8', '#16a34a', '#f59e0b', '#dc2626', '#64748b', '#0f172a', '#14b8a6'];
  new Chart(canvas, {
    type: type,
    data: {
      labels: labels,
      datasets: [{
        data: values,
        backgroundColor: palette,
        borderColor: '#ffffff',
        borderWidth: 1
      }]
    },
    options: {
      responsive: true,
      plugins: { legend: { position: 'bottom' } },
      scales: type === 'bar' || type === 'line' ? { y: { beginAtZero: true } } : {}
    }
  });
}
