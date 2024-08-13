function selectColor(element) {
    var siblings = element.parentNode.children;
    for (var i = 0; i < siblings.length; i++) {
        siblings[i].classList.remove('outline');
    }
    element.classList.add('outline');
}

document.querySelectorAll('.size-option').forEach(function(element) {
    element.addEventListener('click', function(event) {
        event.preventDefault();
        var selectedSize = event.target.getAttribute('data-size');
        document.getElementById('selected-size').textContent = selectedSize;
    });
});

function updateQuantity(change) {
    const qtyInput = document.getElementById('qtybutton');
    let qty = parseInt(qtyInput.value, 10) || 1;
    qty += change;
    if (qty < 1) {
        qty = 1;
    }
    qtyInput.value = qty;
}

function submitWishlistForm() {
    document.getElementById('wishlist-form').submit();
}

