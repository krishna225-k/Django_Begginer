from django import forms


class InsertingDataFrom(forms.Form):
    product_id = forms.IntegerField(
        label='Enter Your product ID ',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Id'
            }
        )
    )

    product_name = forms.CharField(
        label="Enter your product name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Name'
            }
        )
    )

    product_price = forms.IntegerField(
        label='Enter Product price',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'product price'
            }
        )
    )

    product_class = forms.CharField(
        label="Enter your product class",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Class'
            }
        )
    )

    customer_name = forms.CharField(
        label='Enter Customer Name',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Customer Name'
            }
        )
    )

    mobile = forms.IntegerField(
        label='Enter Mobile number',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your mobile '
            }
        )
    )

    email = forms.EmailField(
        label='Enter Email Id',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'YOur email ID'
            }
        )
    )


class UpdateDataForm(forms.Form):
    product_id = forms.IntegerField(
        label=" Enter product Id",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Id'
            }
        )
    )

    product_id = forms.IntegerField(
        label=" Enter product price",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product price'
            }
        )
    )


class DeletingDataForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter product ID",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Product Id'
            }
        )
    )
