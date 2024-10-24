# routes.py

from app import app, collection
from flask import render_template, redirect, url_for, flash, request, jsonify
from datetime import datetime
from forms import AddBookForm, EditBookForm, DeleteBookForm
from bson import ObjectId  # Import ObjectId

@app.route('/')
@app.route('/index')
def index():
    books = list(collection.find())
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddBookForm()

    if form.validate_on_submit():
        isbn = form.isbn.data
        title = form.title.data
        year = form.year.data
        price = form.price.data
        page = form.page.data
        category = form.category.data
        coverPhoto = form.coverPhoto.data
        publisher = form.publisher.data
        author = form.author.data

        date = datetime.utcnow()
        collection.insert_one({
            "isbn": isbn,
            "title": title,
            "year": year,
            "price": price,
            "page": page,
            "category": category,
            "coverPhoto": coverPhoto,
            "publisher": publisher,
            "author": author,
            "date": date
        })

        flash('The book was added to the database.')
        return redirect(url_for('index'))

    return render_template('add.html', form=form)

@app.route('/edit/<string:book_id>', methods=['GET', 'POST'])
def edit(book_id):
    book = collection.find_one({"_id": ObjectId(book_id)})
    form = EditBookForm()

    if book:
        if form.validate_on_submit():
            title = form.title.data
            date = datetime.utcnow()
            collection.update_one({"_id": ObjectId(book_id)}, {"$set": {"title": title, "date": date}})
            flash('The book in the database was updated.')
            return redirect(url_for('index'))
        form.title.data = book['title']
        return render_template('edit.html', form=form, book_id=book_id, book=book)  # Pass 'book' variable to the template
    else:
        flash('The book ID is not in the database.')
        return redirect(url_for('index'))


@app.route('/delete/<string:book_id>', methods=['GET', 'POST'])
def delete(book_id):
    book = collection.find_one({"_id": ObjectId(book_id)})  # Use ObjectId
    form = DeleteBookForm()

    if book:
        if form.validate_on_submit():
            collection.delete_one({"_id": ObjectId(book_id)})  # Use ObjectId
            flash('The book in the database was deleted.')
            return redirect(url_for('index'))
        return render_template('delete.html', form=form, book_id=book_id, title=book['title'])
    else:
        flash('The book ID is not in the database.')
        return redirect(url_for('index'))

# Updated route for CRUD operations
@app.route('/crud/<string:operation>/<string:book_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def crud(operation, book_id):
    book = collection.find_one({"_id": ObjectId(book_id)})

    if operation == 'view':
        return render_template('view.html', book=book)

    form = EditBookForm()

    if request.method == 'GET':
        # Handle GET request
        if operation == 'edit':
            form.title.data = book['title']
            return render_template('edit.html', form=form, book_id=book_id)
        elif operation == 'delete':
            return render_template('delete.html', form=form, book_id=book_id, title=book['title'])
        else:
            flash('Invalid operation.')
            return redirect(url_for('index'))

    elif request.method == 'POST':
        # Handle POST request
        if operation == 'edit' and form.validate_on_submit():
            title = form.title.data
            date = datetime.utcnow()
            collection.update_one({"_id": ObjectId(book_id)}, {"$set": {"title": title, "date": date}})
            flash('The book in the database was updated.')
            return redirect(url_for('index'))
        elif operation == 'delete' and form.validate_on_submit():
            collection.delete_one({"_id": ObjectId(book_id)})
            flash('The book in the database was deleted.')
            return redirect(url_for('index'))
        else:
            flash('Invalid operation.')
            return redirect(url_for('index'))

    elif request.method == 'PUT':
        # Handle PUT request (using JSON for simplicity)
        data = request.get_json()
        title = data.get('title')
        date = datetime.utcnow()
        collection.update_one({"_id": ObjectId(book_id)}, {"$set": {"title": title, "date": date}})
        return jsonify({"message": "Book updated successfully"})

    elif request.method == 'DELETE':
        # Handle DELETE request (using JSON for simplicity)
        collection.delete_one({"_id": ObjectId(book_id)})
        return jsonify({"message": "Book deleted successfully"})

    else:
        flash('Invalid method.')
        return redirect(url_for('index'))
