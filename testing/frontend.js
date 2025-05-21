fetch('http://localhost:3000/data')
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById('data-container');
        container.textContent = JSON.stringify(data);
    })
    .catch(error => {
        console.error('Error fetching data:', error);
    });
