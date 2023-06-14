from django import forms
from django.forms import CheckboxSelectMultiple


from .models import Criteria, NiokrUser, Project, NiokrProject, NiokrCriteria, Equipment


class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("name", "site", "description", "tag", "note", "cover")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class EquipmentCreateForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ("name", "characteristic", "owner", "contact", "image")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class ProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("name", "cover", "site", "tag", "description", "note")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class ProjectAddResponsibleForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ("responsible",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"


class CriteriaForm(forms.ModelForm):
    class Meta:
        model = Criteria
        fields = ("science", "interesting", "difficult", "unclear", "repeat")


class NiokrProjectCreateForm(forms.ModelForm):
    class Meta:
        model = NiokrProject
        fields = (
            "theme",
            "site",
            "data_project_start",
            "base_organisation",
            "science_novelty",
            "commercial_result",
            "equipment",
            "grants",
            "patents",
            "cover",
            "annotation",
            "responsible",
            "team",
        )
        widgets = {
            "data_project_start": forms.DateInput(
                format=("%d-%m-%Y"),
                attrs={"placeholder": "Выберите дату"},
            ),
            "team": CheckboxSelectMultiple(),
        }

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["responsible"].queryset = NiokrUser.objects.filter(
            user=user, is_responsible=True
        )
        self.fields["team"].queryset = NiokrUser.objects.filter(
            user=user, is_responsible=False
        )
        self.fields["theme"].widget.attrs["class"] = "form-control"
        self.fields["site"].widget.attrs["class"] = "form-control"
        self.fields["data_project_start"].widget.attrs["class"] = "form-control"
        self.fields["base_organisation"].widget.attrs["class"] = "form-control"
        self.fields["science_novelty"].widget.attrs["class"] = "form-control"
        self.fields["commercial_result"].widget.attrs["class"] = "form-control"
        self.fields["equipment"].widget.attrs["class"] = "form-control"
        self.fields["grants"].widget.attrs["class"] = "form-control"
        self.fields["patents"].widget.attrs["class"] = "form-control"
        self.fields["cover"].widget.attrs["class"] = "form-control"
        self.fields["annotation"].widget.attrs["class"] = "form-control"
        self.fields["responsible"].widget.attrs["class"] = "form-control"


class NiokrProjectUpdateForm(forms.ModelForm):
    class Meta:
        model = NiokrProject
        fields = (
            "theme",
            "site",
            "data_project_start",
            "base_organisation",
            "science_novelty",
            "commercial_result",
            "equipment",
            "grants",
            "patents",
            "cover",
            "annotation",
            "responsible",
            "team",
        )
        widgets = {"team": forms.CheckboxSelectMultiple()}

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["responsible"].queryset = NiokrUser.objects.filter(
            user=user, is_responsible=True
        )
        self.fields["team"].queryset = NiokrUser.objects.filter(
            user=user, is_responsible=False
        )
        self.fields["theme"].widget.attrs["class"] = "form-control"
        self.fields["site"].widget.attrs["class"] = "form-control"
        self.fields["data_project_start"].widget.attrs["class"] = "form-control"
        self.fields["base_organisation"].widget.attrs["class"] = "form-control"
        self.fields["science_novelty"].widget.attrs["class"] = "form-control"
        self.fields["commercial_result"].widget.attrs["class"] = "form-control"
        self.fields["equipment"].widget.attrs["class"] = "form-control"
        self.fields["grants"].widget.attrs["class"] = "form-control"
        self.fields["patents"].widget.attrs["class"] = "form-control"
        self.fields["cover"].widget.attrs["class"] = "form-control"
        self.fields["annotation"].widget.attrs["class"] = "form-control"
        self.fields["responsible"].widget.attrs["class"] = "form-control"


class NiokrCriteriaForm(forms.ModelForm):
    class Meta:
        model = NiokrCriteria
        fields = ("science", "interesting", "difficult", "unclear", "repeat")


class NiokrUserCreate(forms.ModelForm):
    class Meta:
        model = NiokrUser
        fields = (
            "fullname",
            "phone",
            "email",
            "academic_degrees",
            "academic_titles",
            "is_responsible",
            "ec_id",
            "photo",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field == "is_responsible":
                continue
            self.fields[field].widget.attrs["class"] = "form-control"
