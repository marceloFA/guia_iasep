var citySlug;
var serviceSlug;

// Open the navigation dropdown
function openNav(navId, elm) {
    document.getElementById(navId).style.height = "100%";
    
};

// Closes the navigation dropdown
function closeNav(navId) {
    document.getElementById(navId).style.height = "0%";
};


// Fill either the select city button or the select service button
// inner text with the dropdown selected button text
function fillButton(buttonId, navId, text, slug) {
    
    if(navId == "serviceNav") serviceSlug = slug;
    if(navId == "cityNav") citySlug = slug;

    // fill the button with the selected button text and close the nav
    document.getElementById(buttonId).innerText = text;
    closeNav(navId);
    };

// route the user to the correct 'city' or 'service in a city' page
function routeTo(citySlug, serviceSlug){
    
    if (!citySlug && !serviceSlug){
        alert("Por favor, selecione uma cidade e um serviço!");
    }
    
    else if (citySlug && !serviceSlug){
        alert("Por favor, selecione um serviço");
    }
    
    else if (citySlug && serviceSlug){
        document.getElementById('route-to').href = `/${citySlug}/${serviceSlug}`;
    }
};