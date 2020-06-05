from typing import List
from formaster.interactors.storages.form_storage_interface import \
    FormStorageInterface
from formaster.models.form import Form
from formaster.models import AssignForm
from formaster.dtos.dtos import FormTitleWithIdDto
from formaster.exceptions.exceptions import (
    InvalidFormId,
    UserIsNotCreaterOfForm
)


class FormStorageImplimentation(FormStorageInterface):

    def add_form_title(self, user_id: int,
                       form_title: str) -> FormTitleWithIdDto:
        form_obj = Form.objects.create(
            created_by_id=user_id,
            form_title=form_title
        )
        form_title_with_id_dto = self._convert_form_object_to_dto(form_obj)
        return form_title_with_id_dto

    @staticmethod
    def _convert_form_object_to_dto(form_obj):
        form_title_with_id_dto = FormTitleWithIdDto(
            form_title=form_obj.form_title,
            form_id=form_obj.id
        )
        return form_title_with_id_dto


    def get_forms(self, user_id: int) -> List[FormTitleWithIdDto]:
        list_of_form_objs = Form.objects.filter(created_by_id=user_id)

        list_of_form_titles_with_id_dto = []
        for form_obj in list_of_form_objs:
            form_title_with_id_dto = self._convert_form_object_to_dto(
                    form_obj
            )
            list_of_form_titles_with_id_dto.append(form_title_with_id_dto)
        return list_of_form_titles_with_id_dto


    def get_user_forms(self, user_id: int) -> List[FormTitleWithIdDto]:
        list_of_form_objs = AssignForm.objects.filter(user_id=user_id)\
                                              .select_related("form")
        list_of_form_titles_with_id_dto = []
        for form_obj in list_of_form_objs:
            form_title_with_id_dto = FormTitleWithIdDto(
                form_id=form_obj.form_id,
                form_title=form_obj.form.form_title
            )
            list_of_form_titles_with_id_dto.append(form_title_with_id_dto)
        return list_of_form_titles_with_id_dto

    def validate_form_id(self, form_id: int) -> bool:
        try:
            Form.objects.get(id=form_id)
        except Form.DoesNotExist:
            raise InvalidFormId
        return True


    def validate_is_user_creater_of_form(
            self, user_id: int, form_id: int) -> bool:
        try:
            Form.objects.get(id=form_id, created_by_id=user_id)
        except Form.DoesNotExist:
            raise UserIsNotCreaterOfForm
        return True


    def delete_form(self, form_id: int):
        form_obj = Form.objects.get(id=form_id)
        form_obj.delete()

    def update_form_title(self, form_id: int, new_form_title: str):
        form_obj = Form.objects.get(id=form_id)
        form_obj.form_title = new_form_title
        form_obj.save()
        form_title_with_id_dto = self._convert_form_object_to_dto(form_obj)
        return form_title_with_id_dto
