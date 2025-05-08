from rekognition_utils import detect_labels, detect_text
from opensearch_utils import bulk_index_data

def process_images(s3_bucket, s3_keys):
    """
    Process each image in the S3 bucket and index metadata into OpenSearch.
    """
    all_metadata = []

    for s3_key in s3_keys:
        try:
            # Get Rekognition labels and text for each image
            labels = detect_labels(s3_bucket, s3_key)
            text_detected = detect_text(s3_bucket, s3_key)

            # Prepare the metadata to index into OpenSearch
            metadata = {
                "image_id": s3_key,  # Use the S3 key as a unique ID for the image
                "label": ", ".join([label['Name'] for label in labels]),
                "text_detected": ", ".join([text['DetectedText'] for text in text_detected]),
                "image_url": f"s3://{s3_bucket}/{s3_key}"
            }

            all_metadata.append(metadata)
        
        except Exception as e:
            print(f"Error processing {s3_key}: {e}")
            continue  # Skip this image and continue with the rest

    # Index the collected metadata into OpenSearch
    bulk_index_data(all_metadata)

def main():
    # S3 Bucket and image file keys (you'll need to provide the correct S3 bucket name and keys)
    s3_bucket = 'eycrowdtesting'
    #s3_keys = ['00a5f471-f033-411a-b8f4-6589a9ccfdc9.jpg', '0a0b16c2-2c9e-4763-94da-a4d139b91754.jpg', '0a20af15-41c2-4bf2-b9f3-4a57710ba0dd.png']  # Example list of image file names in S3
    s3_keys = [
    '0b7b31af-5d7b-4dbd-8cdf-387df555af98.jpg',
    '0bb694f0-9362-4572-a20c-a5993089a6fc.jpg',
    '1ce17a32-c2cb-4223-8198-85f54a2f3159.jpg',
    '0a21c854-5879-45b4-bd1a-6fd5571d3e7d.jpg',
    '01a0cc30-18f0-46f1-b4f2-530f7a63d30a.jpg',
    '0aeac812-1268-497e-88c1-f48ef14c112f.jpg',
    '0a235d7b-9152-45ae-8c8e-c8a35cbf5413.jpg',
    '0fe6c643-deba-4dec-a274-af66f7f594d4.jpg',
    '0b8ea072-4b15-41a7-bd8f-f0d06586c746.jpg',
    '0ab7115f-2edd-4375-bd4f-969efa67b36c.jpg',
    '0dd84ad4-da9b-4b9c-a8f9-9336207d18f6.png',
    '0a3a1f71-86df-42b6-a9b2-c90474543f8a.jpg',
    '0b6872d4-bde3-4f36-b51f-9a817eaaa6fc.jpg',
    '1c943bef-1569-4228-9d51-1c9de2727334.png',
    '1ecd5536-3d35-4f42-ad8c-ca23ce4e34eb.jpg',
    '1c5ed443-f7bc-40ac-88ee-d80a43e47b5a.jpg',
    '0b1a3194-2fcd-4d4d-841a-660eb7c0bdd5.jpg',
    '0a0b16c2-2c9e-4763-94da-a4d139b91754.jpg',
    '0abe6b09-ee18-475f-a0c4-1b39206682c9.jpg',
    '0b749274-ebde-44af-9116-f13ec57a73e0.jpg',
    '0a1deceb-ad66-44ef-8f72-38af893d1f27.jpg',
    '1ab5a86e-fafc-4fe0-87e9-08f858bacbde.jpg',
    '1bb890b1-fff2-4124-88c0-488c85da95e5.jpg',
    '1b2619ca-838c-4ae5-8067-74052390934c.jpg',
    '0b090128-8d9e-442c-8539-483fc6b0449f.jpg',
    '0b7ec58b-218b-4a5e-b988-1ba1f3bf25f3.jpg',
    '0cada5e0-6086-4dbb-9cc8-859724ccd21e.png',
    '1d3bd045-e84a-4181-9dd9-ba2b2fc93660.jpg',
    '0b3910a8-426c-4db8-a88c-dc20e5a4eb8e.jpg',
    '1c529542-186e-441e-958c-ac21cc540dae.jpg',
    '0a679367-954f-489c-a3dc-d1ed23adeee1.jpg',
    '2a2e71b7-c801-4c9e-9468-496855ac5490.jpg',
    '0bb51956-fb90-4da9-93be-a270730147e5.jpg',
    '0a6b9210-ee01-4451-83e1-2171beb0e398.jpg',
    '0bc6d868-1fe8-4194-9da5-cbc1c1e1cf3b.jpg',
    '0f97da89-6836-4370-9030-8043ad071194.jpg',
    '0a5d6c8d-505b-4566-b99d-8b7d9ff09b9c.jpg',
    '0b77f21b-2048-461f-8152-b34d81fe2e84.jpg',
    '00dbf27c-2006-4e7f-ab7d-a2632508cc00.jpg',
    '2a16a527-f3bd-4b26-9c67-1ea64fa48ae2.jpg',
    '1fbe85da-b7c5-46fc-af6f-c9f171a1b15c.jpg',
    '2a93bd67-3563-47d9-8671-138cc7a5e3da.jpg',
    '1ec4f71f-867b-45fa-a464-4d1ba0cf861e.jpg',
    '1af2e50d-f547-4b63-867f-5846cb9580e0.jpg',
    '0b8b7fe5-b41e-42d5-99b0-33c5a3fe1c04a3.jpg',
    '00d14b75-3224-4f6e-89e9-63e6eb03ccd4.jpg',
    '00b38943-6a31-4b16-ac21-ec066643b977.jpg',
    '0c0a0c8f-804c-4e35-a9c4-1b3d5ee16f0f.png',
    '0a527218-cdc8-4fce-a9eb-8bbe0836fb92.jpg',
    '1ebe2a44-75b4-4e33-932c-361b9152e90b.jpg',
    '00a5f471-f033-411a-b8f4-6589a9ccfdc9.jpg',
    '1c36937d-57c3-4ab3-84b1-bbb5b6899662.jpg',
    '1f47f6ee-4ba9-439f-82a2-2f4eba644a30.jpeg',
    '0a6bde3a-90df-4cd7-b22b-38332e9519c7.jpg',
    '2a1dbe01-3ac0-4933-a38e-0a3234661930.jpg',
    '1ad6ef7d-8fcf-482a-a981-bd3b9cd546b5.jpg',
    '0ab9c29a-edb7-4daa-8c1b-0bc56f0ce5f7.jpg',
    '0b964941-d317-4722-949b-1755bf42182e.jpg',
    '0b4e810b-321e-4933-b5fb-fa5b6d04a840.jpg',
    '1a07dc46-ff42-4cbd-b2e7-4aad864b5706.jpg',
    '1f87b272-c954-47f1-a42b-e3d466a5a252.jpg',
    '0af372ec-b223-4e8f-87ff-f79d41664ba9.jpg',
    '1f7c7fdc-5c79-4426-a34c-a452f6cff89d.jpg',
    '0bbb96c0-062a-441e-84c9-66e288372012.png',
    '0b0ac236-9b85-46cb-a5ea-5bc8e668028f.jpg',
    '0ac44424-0ac3-4234-b31a-12828725d7d5.jpg',
    '1ea94924-1a8b-4b4e-b686-b69e69bce7dd.jpg',
    '1b9b5c2a-fac9-44be-9ac6-b808007cfc24.jpg',
    '0b406f80-d976-4b6e-8626-f4706f1fcdb6.jpg',
    '1b78b8a4-8e12-4665-932a-e7146072add7.jpg',
    '0f0cc600-0953-4f94-a438-b9b3e9b394e4.jpg',
    '1d922814-769c-4c0a-acd4-76849414a04f.jpg',
    '0c1b03fe-383e-4d68-a36b-bd1b2f6566a3.jpg',
    '0ab66e69-5c06-46d4-939a-13e1b87c4811.jpg',
    '0ba6575e-bb5b-4654-9ecb-782eb6e711f5.jpg',
    '0a3ff83c-5c21-474c-b086-fc08358fad9b.jpg',
    '1e833a61-e809-4f79-9bc9-37c770e60962.jpg',
    '0b2f2d61-4fe1-4396-a153-8d0558a219e2.jpg',
    '1c0ff18b-8c25-4c9f-a892-89a6973aeb23.jpg',
    '0ef400ce-f4bf-4705-ae70-ba88e9fc63b1.jpg',
    '0a99c863-dbf8-409c-a022-c9712ad28957.png',
    '0a20af15-41c2-4bf2-b9f3-4a57710ba0dd.png',
    '1f19f0b1-c3c9-437f-b6d6-2dca881a1122.jpg',
    '1fcd2aee-41f2-40b3-b6dd-6075261b4d54.jpg',
    '0b1f9fa6-904d-4540-aba2-15088007645e.png',
    '0a6ce4d5-6e1c-45cc-bd46-f5c8b20283e8.jpg',
    '0d3f08e4-4cd4-46dc-ae98-852eec726acc.png',
    '0ff5aa00-709e-4e16-979e-f0bf88cc135c.jpg',
    '0b944d6d-726e-48d7-9c73-efe175052c8e.jpg',
    '1abe645d-b7fd-4466-86b2-8411189fcf5e.jpg'
]

    # Process images and extract metadata using Rekognition
    process_images(s3_bucket, s3_keys)
    print("Images processed and indexed into OpenSearch.")

if __name__ == '__main__':
    main()
