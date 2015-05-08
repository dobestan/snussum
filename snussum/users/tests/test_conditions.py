from django.test import TestCase

from django.contrib.auth.models import User


class ConditionsTest(TestCase):
    def setUp(self):
        self.boy = User.objects.create_user(username="test_boy")
        self.girl = User.objects.create_user(username="test_girl")

    def test_age_conditions_without_any_conditions(self):
        # 나이조건이 없는 경우, 나이, 나이조건에 관계 없이 매칭이 가능하다
        self.assertTrue(self.boy.userprofile.is_age_condition_available_with(self.girl))
        self.assertTrue(self.girl.userprofile.is_age_condition_available_with(self.boy))

    def test_age_conditions_with_conditions(self):
        # 나이조건이 있는 경우, 이 나이조건에 부합하는지 체크한다.
        
        # 나이조건이 없고, 상대방의 나이만 설정되어 있을 경우 매칭이 가능하다.
        self.girl.userprofile.age = 20
        self.girl.userprofile.save()
        
        self.girl = User.objects.get(id=self.girl.id)
        self.boy = User.objects.get(id=self.boy.id)

        self.assertTrue(self.boy.userprofile.is_age_condition_available_with(self.girl))
        self.assertTrue(self.girl.userprofile.is_age_condition_available_with(self.boy))

        # 나이조건이 있고, 상대방의 나이가 나이조건에 포함되는 경우 매칭이 가능하다.
        self.boy.userprofile.age_condition = (19, 25)
        self.boy.userprofile.save()

        self.girl = User.objects.get(id=self.girl.id)
        self.boy = User.objects.get(id=self.boy.id)


        self.assertTrue(self.boy.userprofile.is_age_condition_available_with(self.girl))
        self.assertTrue(self.girl.userprofile.is_age_condition_available_with(self.boy))

        # 나이조건이 있고, 상대방의 나이가 나이조건에 포함되지 않는 경우 매칭이 가능하지 않다.
        self.boy.userprofile.age_condition = (25, 28)
        self.boy.userprofile.save()

        self.girl = User.objects.get(id=self.girl.id)
        self.boy = User.objects.get(id=self.boy.id)

        self.assertFalse(self.boy.userprofile.is_age_condition_available_with(self.girl))
        self.assertTrue(self.girl.userprofile.is_age_condition_available_with(self.boy))

        # 나이조건이 있고, 상대방의 나이가 입력되지 않는 경우 매칭이 가능하지 않다.
        self.girl.userprofile.age = None
        self.girl.userprofile.save()
        
        self.girl = User.objects.get(id=self.girl.id)
        self.boy = User.objects.get(id=self.boy.id)

        self.assertFalse(self.boy.userprofile.is_age_condition_available_with(self.girl))
        self.assertTrue(self.girl.userprofile.is_age_condition_available_with(self.boy))
