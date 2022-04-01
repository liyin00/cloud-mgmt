from google.cloud import storage

GCS_PROJECT = 'elegant-fort-344208' # i.e. Google Cloud project name
GCS_BUCKET = 'clae_frontend_bucket' # i.e. Google Cloud bucket name

main_page_suffix="error.html"
not_found_page="error.html"

client = storage.Client.from_service_account_json('./elegant-fort-344208-8b484a00d773.json')
bucket = client.get_bucket(GCS_BUCKET)
bucket.configure_website(main_page_suffix, not_found_page)
bucket.patch()

print(
    "Static website bucket {} is set up to use {} as the index page and {} as the 404 page".format(
        bucket.name, main_page_suffix, not_found_page
    )
)