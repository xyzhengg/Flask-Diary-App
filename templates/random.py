@app.route('/addentry', methods=['GET', 'POST'])
def addentry():
    if session.get('user_id') is None:
        return redirect ('/login')
    user_name = session.get('user_name')
    if request.method == 'GET':
        diary_id=session.get('diary_id')
        users = get_all_username(diary_id)
        user_one = users[0]['first_name'].capitalize()
        user_two = users[1]['first_name'].capitalize()
        return render_template('new_entry.html',
                               user_name=user_name,
                               user_one = user_one,
                               user_two = user_two)
    if request.method == 'POST':
        diary_code = session.get('diary_id')
        user_id = session.get('user_id')
        diary_heading = request.form.get('heading').capitalize()
        diary_text = request.form.get('entry').capitalize()

        entry_id = add_entry(diary_code, user_id, diary_heading, diary_text)
        post_id = entry_id['id']

        images = request.files.getlist('images')
        if len(images) > 0:
            image_rows = []
            for image in images:
                if image.filename != '': 
                    uploaded_image = cloudinary.uploader.upload(image)
                    image_rows.append([uploaded_image['public_id'], uploaded_image['url'], entry_id['id']])
            insert_many_images(image_rows)
        return redirect(f'/view/{post_id}')