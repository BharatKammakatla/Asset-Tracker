from flask_login import login_required
from app.asset.forms import AddAssetForm, EditAssetForm
from app.asset import main
from app.asset.models import Transaction
from flask import render_template, flash, request, redirect, url_for
from app import db



@main.route('/')
def display_transactions():
    transactions = Transaction.query.all()
    return render_template('home.html', transactions=transactions)


@main.route('/add/asset', methods=['GET', 'POST'])
@login_required
def add_assset():
    form = AddAssetForm()
    if form.validate_on_submit():
        asset = Transaction(type=form.type.data, asset_name=form.asset_name.data, person_name=form.person_name.data,
                    start_time=form.start_time.data, end_time=None, status=form.status.data)
        db.session.add(asset)
        db.session.commit()
        flash('Asset added successfully')
        return redirect(url_for('main.display_transactions'))
    return render_template('add_asset.html', form=form)


@main.route('/edit/asset/<id>', methods=['GET', 'POST'])
@login_required
def edit_asset(id):
    transaction = Transaction.query.get(id)
    form = EditAssetForm(obj=transaction)
    if form.validate_on_submit():
        transaction.end_time = form.end_time.data
        transaction.status = form.status.data
        db.session.add(transaction)
        db.session.commit()
        flash('Edit successful')
        return redirect(url_for('main.display_transactions'))
    return render_template('edit_asset.html', form=form, id=id)