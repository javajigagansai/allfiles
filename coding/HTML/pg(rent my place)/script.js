document.getElementById('searchForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const location = document.getElementById('location').value;
    const type = document.getElementById('type').value;
    const minPrice = parseInt(document.getElementById('minPrice').value) || 0;
    const maxPrice = parseInt(document.getElementById('maxPrice').value) || Infinity;
    const amenities = document.getElementById('amenities').value;

    // Sample data for demonstration
    const pgsAndHostels = [
        { name: "PG in Delhi", location: "Delhi", type: "PG", price: 8000, vaccine: "Fully Vaccinated", amenities: ["WiFi", "Food"] },
        { name: "Hostel in Bangalore", location: "Bangalore", type: "Hostel", price: 5000, vaccine: "Not Vaccinated", amenities: ["WiFi", "AC"] },
        { name: "PG in Mumbai", location: "Mumbai", type: "PG", price: 12000, vaccine: "Partially Vaccinated", amenities: ["Food"] },
    ]