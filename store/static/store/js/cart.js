console.log('hellow there')

// $(document).ready(
//     $.ajax({
//         Type:"GET",
//         url:"/",
//         success:function(response){
//             console.log("value of response is", response)
//         },
//         error:function(response){
//             // console.log("value of erroe response is ", response)
//         }
//     })
// )


var update_button = $(".update-cart")
for (i = 0; i < update_button.length; i++) {
    $(update_button[i]).on('click', function () {
        var productId = this.dataset.product 
        var action = this.dataset.action
        console.log("productId:", productId, "action:", action) 

        console.log("user:", user)
        if (user == 'AnonymousUser') {
            console.log("value of user", user)
            // getCookieItem(productId, action) 
        } else {
            updateUserOrder(productId, action)
            console.log("value of user", user)
        }
    })

}

// function getCookieItem(productId, action) {

//     if (action == 'add') {
//         if (cart[productId] == undefined) {

//             cart[productId] = { 'quantity': 1 }
//         } else {
//             cart[productId]['quantity'] += 1
//         }
//     }
//     if (action == 'remove') {

//         cart[productId]['quantity'] -= 1
//         if (cart[productId]['quantity'] <= 0) {
//             console.log('remove item')
//             delete cart[productId] 
//         }
//     }
//     console.log('cart:', cart)

//     document.cookie = "cart=" + JSON.stringify(cart) + ";domain;path=/"
//     location.reload()


// }


function updateUserOrder(productId, action) {
    $.ajax({
        type:"POST",
        url: "/update_item/",
        // url:'{% url "updateitemPage" %}',
        data:{
            productId:productId,
            action:action,
        },
        headers:{
            "X-CSRFToken":csrftoken
        },
        success:function(response){
            console.log(("are under success function", response));
            console.log(response.cartItem)
            var cart_total = $("#cart-total").text(response.cartItem)

            
        },
        error:function(response){
            console.log("you are under error function", response)
            
        }
    });
}
    // delete cart[productId]
    // cart = {}
	// document.cookie = "cart=" + JSON.stringify(cart) + ";domain;path=/"
//     var url = "/update_item/"
//     fetch(url, {
//         method: "POST",
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrftoken
//         },
//         body: JSON.stringify({
//             'productId': productId,
//             'action': action
//         })

//     })
//         .then(response => {
//             return response.json()
//         })
//         .then(data => {
//             console.log('data:', data)
//             // location.reload()
//         })
// }