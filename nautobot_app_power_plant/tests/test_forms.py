"""Test nautobotapppowerplantexamplemodel forms."""

from django.test import TestCase

from nautobot_app_power_plant import forms


class UPSModelTest(TestCase):
    """Test UPSModel forms."""

    def test_specifying_all_fields_success(self):
        form = forms.UPSModelForm(
            data={
                "name": "Development",
                "description": "Development Testing",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_specifying_only_required_success(self):
        form = forms.UPSModelForm(
            data={
                "name": "Development",
            }
        )
        self.assertTrue(form.is_valid())
        self.assertTrue(form.save())

    def test_validate_name_nautobotapppowerplantexamplemodel_is_required(self):
        form = forms.UPSModelForm(data={"description": "Development Testing"})
        self.assertFalse(form.is_valid())
        self.assertIn("This field is required.", form.errors["name"])
