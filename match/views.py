from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import UserSerializer
from .models import FemaleDatingQueue, FemaleDrinkQueue, FemaleGymQueue, FemalePartyQueue, MaleDatingQueue, MaleDrinkQueue, MaleGymQueue, MalePartyQueue, MaleQueue, FemaleQueue
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

import logging

User = get_user_model()

class AddToQueueAndMatchView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        need = request.data.get('need')  # ユーザーのニーズを取得 (例: 'gym', 'drink', 'party', 'dating')

        # ニーズに基づいて対応するキューを決定
        if need == 'gym':
            male_queue_class = MaleGymQueue
            female_queue_class = FemaleGymQueue
        elif need == 'drink':
            male_queue_class = MaleDrinkQueue
            female_queue_class = FemaleDrinkQueue
        elif need == 'party':
            male_queue_class = MalePartyQueue
            female_queue_class = FemalePartyQueue
        elif need == 'dating':
            male_queue_class = MaleDatingQueue
            female_queue_class = FemaleDatingQueue
            if user.sex == 'Male':
                female_queue = female_queue_class.objects.first()

                # 女性キューにユーザーがいれば即時マッチング
                if female_queue and female_queue.users.exists():
                    matched_user = female_queue.users.first()

                    # マッチング処理
                    user.cur_matching = matched_user
                    matched_user.cur_matching = user

                    user.wait = False
                    matched_user.wait = False
                    user.done = False
                    matched_user.done = False

                    user.save()
                    matched_user.save()

                    # 女性キューからマッチしたユーザーを削除
                    female_queue.users.remove(matched_user)

                    return Response({
                        'status': 'Matched',
                        'matched_user': matched_user.email  # 必要に応じて名前や他の情報も追加可能
                    }, status=status.HTTP_200_OK)

                else:
                    male_queue, created = male_queue_class.objects.get_or_create()
                    male_queue.users.add(user)
                    user.wait = True
                    user.save()

                    return Response({
                        'status': 'Added to male queue, waiting for match'
                    }, status=status.HTTP_200_OK)
            elif user.sex == 'Female':
                male_queue = male_queue_class.objects.first()

                # 男性キューにユーザーがいれば即時マッチング
                if male_queue and male_queue.users.exists():
                    matched_user = male_queue.users.first()

                    # マッチング処理
                    user.cur_matching = matched_user
                    matched_user.cur_matching = user

                    user.wait = False
                    matched_user.wait = False
                    user.done = False
                    matched_user.done = False

                    user.save()
                    matched_user.save()

                    # 男性キューからマッチしたユーザーを削除
                    male_queue.users.remove(matched_user)

                    return Response({
                        'status': 'Matched',
                        'matched_user': matched_user.email  # 必要に応じて名前や他の情報も追加可能
                    }, status=status.HTTP_200_OK)
                else:
                    female_queue, created = female_queue_class.objects.get_or_create()
                    female_queue.users.add(user)
                    user.wait = True
                    user.save()

                    return Response({
                        'status': 'Added to female queue, waiting for match'
                    }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid gender'}, status=status.HTTP_400_BAD_REQUEST)
        elif need == 'friend':
            male_queue_class = MaleQueue
            female_queue_class = FemaleQueue
        else:
            return Response({'error': 'Invalid need type'}, status=status.HTTP_400_BAD_REQUEST)

        # ユーザーの性別に基づいて対応するキューでマッチングを実行
        if user.sex == 'Female':
            female_queue = female_queue_class.objects.first()

            # 女性キューにユーザーがいれば即時マッチング
            if female_queue and female_queue.users.exists():
                matched_user = female_queue.users.first()

                # マッチング処理
                user.cur_matching = matched_user
                matched_user.cur_matching = user

                user.wait = False
                matched_user.wait = False
                user.done = False
                matched_user.done = False

                user.save()
                matched_user.save()

                # 女性キューからマッチしたユーザーを削除
                female_queue.users.remove(matched_user)

                return Response({
                    'status': 'Matched',
                    'matched_user': matched_user.email  # 必要に応じて名前や他の情報も追加可能
                }, status=status.HTTP_200_OK)

            else:
                female_queue, created = female_queue_class.objects.get_or_create()
                female_queue.users.add(user)
                user.wait = True
                user.save()

                return Response({
                    'status': 'Added to male queue, waiting for match'
                }, status=status.HTTP_200_OK)

        elif user.sex == 'Male':
            male_queue = male_queue_class.objects.first()

            # 男性キューにユーザーがいれば即時マッチング
            if male_queue and male_queue.users.exists():
                matched_user = male_queue.users.first()

                # マッチング処理
                user.cur_matching = matched_user
                matched_user.cur_matching = user

                user.wait = False
                matched_user.wait = False
                user.done = False
                matched_user.done = False

                user.save()
                matched_user.save()

                # 男性キューからマッチしたユーザーを削除
                male_queue.users.remove(matched_user)

                return Response({
                    'status': 'Matched',
                    'matched_user': matched_user.email  # 必要に応じて名前や他の情報も追加可能
                }, status=status.HTTP_200_OK)

            else:
                male_queue, created = male_queue_class.objects.get_or_create()
                male_queue.users.add(user)
                user.wait = True
                user.save()

                return Response({
                    'status': 'Added to female queue, waiting for match'
                }, status=status.HTTP_200_OK)

        else:
            return Response({'error': 'Invalid gender'}, status=status.HTTP_400_BAD_REQUEST)

# class AddToQueueView(APIView):
#     def post(self, request):
#         user = request.user

#         # ユーザーの性別に基づいてキューを決定
#         if user.sex == 'Male':
#             queue, created = MaleQueue.objects.get_or_create()
#             queue.users.add(user)
#         elif user.sex == 'Female':
#             queue, created = FemaleQueue.objects.get_or_create()
#             queue.users.add(user)
#         else:
#             return Response({'error': 'Invalid gender'}, status=status.HTTP_400_BAD_REQUEST)

#         # ユーザーのステータスを更新
#         user.wait = True
#         user.done = False
#         user.save()

#         return Response({'status': 'User added to queue', 'queue': 'Male' if user.sex == 'male' else 'Female'}, status=status.HTTP_200_OK)
    
# class ProcessMatchingView(APIView):
#     def post(self, request):
#         # 男性キューと女性キューを取得
#         male_queue = MaleQueue.objects.first()
#         female_queue = FemaleQueue.objects.first()

#         if not male_queue and not female_queue:
#             return Response({'error': 'Both queues are empty'}, status=status.HTTP_400_BAD_REQUEST)

#         # 男性キューのマッチング処理
#         if male_queue:
#             male_users = list(male_queue.users.all())
#             num_males = len(male_users)
#             for i in range(0, num_males // 2):
#                 user1 = male_users[i]
#                 user2 = male_users[num_males - i - 1]

#                 user1.cur_matching = user2
#                 user2.cur_matching = user1

#                 user1.wait = False
#                 user2.wait = False

#                 user1.save()
#                 user2.save()

#             # 奇数の場合、真ん中のユーザーを新しいキューに追加
#             if num_males % 2 == 1:
#                 middle_user = male_users[num_males // 2]
#                 new_male_queue = MaleQueue.objects.create()
#                 new_male_queue.users.add(middle_user)

#             # 男性キューのクリア
#             male_queue.users.clear()

#         # 女性キューのマッチング処理
#         if female_queue:
#             female_users = list(female_queue.users.all())
#             num_females = len(female_users)
#             for i in range(0, num_females // 2):
#                 user1 = female_users[i]
#                 user2 = female_users[num_females - i - 1]

#                 user1.cur_matching = user2
#                 user2.cur_matching = user1

#                 user1.wait = False
#                 user2.wait = False

#                 user1.save()
#                 user2.save()

#             # 奇数の場合、真ん中のユーザーを新しいキューに追加
#             if num_females % 2 == 1:
#                 middle_user = female_users[num_females // 2]
#                 new_female_queue = FemaleQueue.objects.create()
#                 new_female_queue.users.add(middle_user)

#             # 女性キューのクリア
#             female_queue.users.clear()

#         return Response({'status': 'Matching process completed, and remaining users moved to a new queue'}, status=status.HTTP_200_OK)
    
class CurrentMatchView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        if user.cur_matching:
            matched_user = user.cur_matching
            serializer = UserSerializer(matched_user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No current match found'}, status=status.HTTP_404_NOT_FOUND)
        
logger = logging.getLogger(__name__)

class SubmitReviewView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        rating = request.data.get('rating')
        
        # デバッグ用ログ
        if rating is None:
            print("Rating is missing in the request.")
        else:
            print(f"Received rating: {rating}")

        if not rating:
            return Response({'error': 'Rating is missing'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            rating = int(rating)
        except ValueError:
            return Response({'error': 'Invalid rating value'}, status=status.HTTP_400_BAD_REQUEST)

        if rating < 1 or rating > 5:
            return Response({'error': 'Rating value must be between 1 and 5'}, status=status.HTTP_400_BAD_REQUEST)

        user = request.user
        matched_user = user.cur_matching
        
        if matched_user is None:
            return Response({'status': 'No current match found to review'}, status=status.HTTP_200_OK)

        # レビューを追加
        matched_user.add_review(rating)

        # マッチング完了処理
        user.done = True
        if matched_user.done:
            matched_user.semi_comp = False
            matched_user.save()
            user.cur_matching = None
        else:
            user.semi_comp = True
            user.cur_matching = None
        user.save()

        return Response({'status': 'Review submitted successfully', 'new_average_rating': matched_user.review_average}, status=status.HTTP_200_OK)