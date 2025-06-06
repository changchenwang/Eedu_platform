# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.db.models import Q

from .models import Course, CourseResource,Video
from operation.models import UserFavorite, CourseComments, UserCourse
from utils.mixin_utils import LoginRequiredMixin

# Create your views here.


class CourseListView(View):
    def get(self, request):
        all_courses = Course.objects.all().order_by("-add_time")

        hot_courses = Course.objects.all().order_by("-click_nums")[:3]

        #Search
        search_keywords = request.GET.get('keywords', "")
        if search_keywords:
            all_courses = all_courses.filter(Q(name__icontains=search_keywords)|Q(desc__icontains=search_keywords)|Q(detail__icontains=search_keywords))


        #course sort
        sort = request.GET.get('sort', "")
        if sort:
            if sort == "students":
                all_courses = all_courses.order_by("-students")
            elif sort == "hot":
                all_courses = all_courses.order_by("-click_nums")

        #page
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 10, request=request)

        courses = p.page(page)

        return render(request, 'course-list.html', {
            "all_courses":courses,
            "sort":sort,
            "hot_courses":hot_courses
        })

# class VideoPlayView(View): #unfinished
#     """
#     video play
#     """
#     def get(self, request, video_id):
#         video = Video.objects.get(id=int(video_id))
#         course = video.lesson.course
#         course.students += 1
#         course.save()
#         #Ask the user if the course has been associated
#         user_courses = UserCourse.objects.filter(user=request.user, course=course)
#         if not user_courses:
#             user_course = UserCourse(user=request.user, course=course)
#             user_course.save()
#
#         user_cousers = UserCourse.objects.filter(course=course)
#         user_ids = [user_couser.user.id for user_couser in user_cousers]
#         all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
#         #Remove all course ids
#         course_ids = [user_couser.course.id for user_couser in all_user_courses]
#         #Get all other courses that the user has learned     XXXXXXXXXXXXX
#         relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
#         all_resources = CourseResource.objects.filter(course=course)
#         return render(request, "course-play.html", {
#             "course":course,
#             "course_resources":all_resources,
#             "relate_courses":relate_courses,
#             "video":video
#         })

class CourseDetailView(View):
    """
    Course details page
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))

        #Increase the number of course clicks
        course.click_nums += 1
        course.save()

        #Whether to favorite the course
        has_fav_course = False
        #Whether to favorite the organization
        has_fav_org = False

        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True

            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True

        tag = course.tag
        if tag:
            relate_coures = Course.objects.filter(tag=tag)[:1]
        else:
            relate_coures = []
        return render(request, "course-detail.html", {
            "course":course,
            "relate_coures":relate_coures,
            "has_fav_course":has_fav_course,
            "has_fav_org":has_fav_org
        })

class CourseInfoView(LoginRequiredMixin, View):
    """
    chapter
    """
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        course.students += 1
        course.save()
        #Ask the user if the course has been associated
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()

        user_cousers = UserCourse.objects.filter(course=course)
        user_ids = [user_couser.user.id for user_couser in user_cousers]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        #Remove all course IDs
        course_ids = [user_couser.course.id for user_couser in all_user_courses]
        #Get all other courses that the user has learned
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
        all_resources = CourseResource.objects.filter(course=course)
        return render(request, "course-video.html", {
            "course":course,
            "course_resources":all_resources,
            "relate_courses":relate_courses
        })

class CommentsView(LoginRequiredMixin, View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_resources = CourseResource.objects.filter(course=course)
        all_comments = CourseComments.objects.all().order_by("-id")
        return render(request, "course-comment.html", {
            "course":course,
            "course_resources":all_resources,
            "all_comments":all_comments

        })


class AddComentsView(View):
    """
    comment
    """
    def post(self, request):
        if not request.user.is_authenticated:
            #login?
            return HttpResponse('{"status":"fail", "msg":"user have not login"}', content_type='application/json')

        course_id = int(request.POST.get("course_id", 0))
        comments = request.POST.get("comments", "")
        if course_id >0 and comments:
            course_comments = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status":"success", "msg":"add successful"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"add failure"}', content_type='application/json')