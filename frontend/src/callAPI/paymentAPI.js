import { loadStripe } from '@stripe/stripe-js';
import env from "react-dotenv";

// export const paymentURL = "http://127.0.0.1:4242";
export const paymentURL = "http://34.142.143.175:4242";

// require('dotenv').config({path: '../../../.env'});

// ====== create ========
//Create payment
export async function checkoutPayment(URL, body) {
    const session = JSON.parse(localStorage.getItem("session"));
    if (session) {
        const user_id = session.user_id;
        if (user_id === "") {
            window.location.href = '/login.html';
            return;
        }
    }
    else {
        window.location.href = '/login.html';
        return;
    }
    
    const stripePromise = loadStripe(env.STRIPE_PK_KEY);
    const stripe = await stripePromise;

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
            console.log("response", response)
            const session = await response.json();
            console.log("session", session)
            console.log("session_id: ", session.id);
            stripe.redirectToCheckout({ sessionId: session.id })
        }
        // const session = await response.json();

        // // When the customer clicks on the button, redirect them to Checkout.
        // const result = await stripe.redirectToCheckout({
        //     sessionId: session.id,
        // });

        // console.log(result)

        // if (result.error){
        //     console.log("error: ", result.error.message)
        // }

    } catch(e) {
        // const error = {
        //     "code": 404,
        //     "error": e
        // }
        console.log("error: ", e)
        return e;
    }
}