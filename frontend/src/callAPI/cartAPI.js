export const cartURL = "http://127.0.0.1:5006";

// ====== create ========
//Create payment
//sample
// export async function getCartByUserId(URL, userId) {
//     try {
//         const data = {
//             method: 'GET',
//             headers: {
//                 'Content-Type': 'application/json'
//             }
//         }
//         const response = await fetch(`${URL}/get_cart_by_user_id/${userId}`)
//         if (response) {
//             const result = await response.json()
//             return result;
//         }
//     } catch(e) {
//         const error = {
//             "code": 404,
//             "error": e
//         }
//         return error;
//     }
// }

export async function getCartByUserId(URL, userId) {
    try {
        console.log("asdass")
        const response = await fetch(`${URL}/get_cart_by_user_id/${userId}`);
        console.log("response is " )
        console.log(response)
        if (response) {
            console.log("enter if ")
            const result = await response.json();
            return result;
        }
    } catch(e) {
        console.log("catch error ")
        const error = {
            "code": 404,
            "error": e
        }
        return error;
    }
}