from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import UserSerializer
from .models import MaleQueue, FemaleQueue
from django.contrib.auth import get_user_model

User = get_user_model()

class AddToQueueView(APIView):
    def post(self, request):
        user = request.user

        # ユーザーの性別に基づいてキューを決定
        if user.sex == 'male':
            queue, created = MaleQueue.objects.get_or_create()
            queue.users.add(user)
        elif user.sex == 'female':
            queue, created = FemaleQueue.objects.get_or_create()
            queue.users.add(user)
        else:
            return Response({'error': 'Invalid gender'}, status=status.HTTP_400_BAD_REQUEST)

        # ユーザーのステータスを更新
        user.wait = True
        user.done = False
        user.save()

        return Response({'status': 'User added to queue', 'queue': 'Male' if user.sex == 'male' else 'Female'}, status=status.HTTP_200_OK)
    
class ProcessMatchingView(APIView):
    def post(self, request):
        # 男性キューと女性キューを取得
        male_queue = MaleQueue.objects.first()
        female_queue = FemaleQueue.objects.first()

        if not male_queue and not female_queue:
            return Response({'error': 'Both queues are empty'}, status=status.HTTP_400_BAD_REQUEST)

        # 男性キューのマッチング処理
        if male_queue:
            male_users = list(male_queue.users.all())
            num_males = len(male_users)
            for i in range(0, num_males // 2):
                user1 = male_users[i]
                user2 = male_users[num_males - i - 1]

                user1.cur_matching = user2
                user2.cur_matching = user1

                user1.wait = False
                user2.wait = False

                user1.save()
                user2.save()

            # 奇数の場合、真ん中のユーザーを新しいキューに追加
            if num_males % 2 == 1:
                middle_user = male_users[num_males // 2]
                new_male_queue = MaleQueue.objects.create()
                new_male_queue.users.add(middle_user)

            # 男性キューのクリア
            male_queue.users.clear()

        # 女性キューのマッチング処理
        if female_queue:
            female_users = list(female_queue.users.all())
            num_females = len(female_users)
            for i in range(0, num_females // 2):
                user1 = female_users[i]
                user2 = female_users[num_females - i - 1]

                user1.cur_matching = user2
                user2.cur_matching = user1

                user1.wait = False
                user2.wait = False

                user1.save()
                user2.save()

            # 奇数の場合、真ん中のユーザーを新しいキューに追加
            if num_females % 2 == 1:
                middle_user = female_users[num_females // 2]
                new_female_queue = FemaleQueue.objects.create()
                new_female_queue.users.add(middle_user)

            # 女性キューのクリア
            female_queue.users.clear()

        return Response({'status': 'Matching process completed, and remaining users moved to a new queue'}, status=status.HTTP_200_OK)
    
class CurrentMatchView(APIView):
    def get(self, request):
        user = request.user
        if user.cur_matching:
            matched_user = user.cur_matching
            serializer = UserSerializer(matched_user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No current match found'}, status=status.HTTP_404_NOT_FOUND)