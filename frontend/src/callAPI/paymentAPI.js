export const URL = "http://127.0.0.1:5005";

// ====== create ========
//Create payment
export async function checkoutPayment(URL, body) {
    try {
        const data = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        }
        const response = await fetch(`${URL}/create-checkout-session`, data)
        if (response) {
            const result = await response.json()
            return result;
        }
    } catch(e) {
        const error = {
            "code": 404,
            "error": e
        }
        return error;
    }
}