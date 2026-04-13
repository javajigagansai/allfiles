const rooms = [
    {
      id: 1,
      type: "PG",
      name: "Luxury PG",
      price: 3500,
      image: "https://via.placeholder.com/300",
      description: "Fully furnished PG with Wi-Fi and meals included."
    },
    {
      id: 2,
      type: "Hostel",
      name: "City Hostel",
      price: 2500,
      image: "https://via.placeholder.com/300",
      description: "A comfortable hostel with great amenities."
    },
    {
      id: 3,
      type: "PG",
      name: "Comfort PG",
      price: 5000,
      image: "https://via.placeholder.com/300",
      description: "Affordable PG with 24/7 security and housekeeping."
    },
    {
      id: 4,
      type: "Hostel",
      name: "Student Hostel",
      price: 4000,
      image: "https://via.placeholder.com/300",
      description: "Student-friendly hostel with common areas."
    }
  ];
  
  const priceInput = document.getElementById("price");
  const priceValue = document.getElementById("priceValue");
  const roomList = document.getElementById("room-list");
  
  priceInput.addEventListener("input", function () {
    priceValue.textContent = "₹" + priceInput.value;
  });
  
  function filterRooms() {
    const selectedType = document.getElementById("type").value;
    const maxPrice = parseInt(priceInput.value);
  
    const filteredRooms = rooms.filter(room => {
      const isTypeMatch = !selectedType || room.type === selectedType;
      const isPriceMatch = room.price <= maxPrice;
      return isTypeMatch && isPriceMatch;
    });
  
    displayRooms(filteredRooms);
  }
  
  function displayRooms(filteredRooms) {
    roomList.innerHTML = "";  // Clear existing rooms
  
    filteredRooms.forEach(room => {
      const roomDiv = document.createElement("div");
      roomDiv.classList.add("room");
  
      roomDiv.innerHTML = `
        <img src="room.image" alt="{room.name}">
        <h3>room.name</h3>
        <p>{room.description}</p>
        <p><strong>Price: ₹${room.price}</strong></p>
      `;
  
      roomList.appendChild(roomDiv);
    });
  }
  