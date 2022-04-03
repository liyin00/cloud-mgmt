// export const productURL = "http://127.0.0.1:5005";
export const productURL = "http://34.143.189.229:5005";

// ====== create ========
//Create payment

export async function getProductById(URL, productId) {
    try {
        const response = await fetch(`${URL}/get_product_by_id/${productId}`);
        if (response) {
            const result = await response.json();
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

export async function getAllProducts(URL) {
    try {
        const response = await fetch(`${URL}/get_product_list`);
        if (response) {
            const result = await response.json();
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