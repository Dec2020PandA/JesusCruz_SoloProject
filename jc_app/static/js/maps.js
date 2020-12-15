        async .defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyANSa6cfMphOZNO4JGnoiyrFf4VwO8c_NE&callback=initMap"
        type="text/javascript"
    
        function initMap() {
            const uluru = { lat: 40.613953, lng: -75.477791 };
            const map = new google.maps.Map(document.getElementById("map"), {
                zoom: 12,
                center: uluru,
            });
            const marker = new google.maps.Marker({
                position: uluru,
                map: map,
            });
        }
    