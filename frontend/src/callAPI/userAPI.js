// export const userURL = "http://127.0.0.1:5003";
export const userURL = "http://34.142.179.188:5003";

// ====== create ========
//Create payment

export async function login(URL, body) {
    try {

        const data = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(body)
        }
        const response = await fetch(`${URL}/login`, data)
        if (response) {
            console.log("SUCCESS")
            const result = await response.json()
            return result;
        }
    } catch(e) {
        console.log("ERROR")
        const error = {
            "code": 404,
            "error": e
        }
        return error;
    }
}