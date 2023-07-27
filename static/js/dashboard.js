// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function () {
    // Initialize map
    let mymap = L.map("map").setView([0, 0], 2);
  
    // Add the tile layer (OpenStreetMap)
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(mymap);
  
    // Function to add markers to the map
    function addMarkers(data) {
      for (let i = 0; i < data.length; i++) {
        let latitude = parseFloat(data[i].latitude); 
        let longitude = parseFloat(data[i].longitude); 
  
        // Check if latitude and longitude are valid numbers
        if (!isNaN(latitude) && !isNaN(longitude)) {
          let marker = L.marker([latitude, longitude]).addTo(mymap);
  
          // Create a popup for the marker
          let popupContent =
            "<b>Country:</b> " +
            data[i].Country +
            "<br><b>Area:</b> " +
            data[i].Area +
            "<br><b>Species:</b> " +
            data[i].Species +
            "<br><b>Activity:</b> " +
            data[i].Activity +
            "<br><b>Fatal:</b> " +
            data[i]["Fatal (Y/N)"] +
            "<br><b>Type:</b> " + 
            data[i].Type +
            "<br><b>Year:</b> " +
            data[i].Year;
  
          marker.bindPopup(popupContent);
        }
      }
    }
  
    // Function to fetch data from Flask API based on year and fatal filter
    function fetchData(year, fatal) {
      fetch(`/shark_attacks?year=${year}&fatal=${fatal}`)
        .then((response) => response.json())
        .then((data) => {
          // Clear previous markers
          mymap.eachLayer(function (layer) {
            if (layer instanceof L.Marker) {
              mymap.removeLayer(layer);
            }
          });
  
          // Add new markers based on fetched data
          addMarkers(data);
        })
        .catch((error) => console.error("Error fetching data:", error));
    }
  
    // Function to handle dropdown changes
    function handleDropdownChange() {
      let year = document.getElementById("year").value;
      let fatal = document.getElementById("fatal").value;
      fetchData(year, fatal);
    }
  
    // Add event listeners to dropdowns
    document.getElementById("year").addEventListener("change", handleDropdownChange);
    document.getElementById("fatal").addEventListener("change", handleDropdownChange);
  
    // Fetch initial data with All years and All fatal status
    fetchData("All", "All");
  });
  