from django.shortcuts import render, redirect
from .models import Practice, Exercises
from .forms import AddPracticeForm, AddExercisesForm


def practice_list_view(request):
    practice_list = Practice.objects.filter(user=request.user)
    return render(request, 'practice_list.html',{
        'practice_list': practice_list
    })


def add_practice(request):
    if request.method == "POST":
        form = AddPracticeForm(request.POST)
        if form.is_valid():
            practice = form.save()
            practice.user = request.user
            practice.save()
            return redirect('practice_list')
        else:
            # тут ошибка
            form = AddPracticeForm()
            return render(request, 'practice_add.html', {'message': 'где-то ошибка',
                'form' : form
            })
    else:
        form = AddPracticeForm()
        return render(request, 'practice_add.html', {
            'form': form
        })


def practice_detail(request, p_id):
    practice = Practice.objects.get(id=p_id)
    exercises = Exercises.objects.filter(link=practice)
    return render(request, 'practice_detail.html', {'practice':practice,
                                                    'exercises': exercises
                                                    })


def add_exercises(request, p_id):
    practice = Practice.objects.get(id=p_id)
    if request.method == "POST":
        form = AddExercisesForm(request.POST)
        if form.is_valid():
            descriptions = form.save()
            descriptions.user = request.user
            descriptions.link = practice
            descriptions.save()
            return redirect('practice_detail', p_id)

        else:
            form = AddExercisesForm(request.POST)
            return render(request, 'exercises_add.html', {"form": form,
                                                              "practice": practice,
                                                          'message': 'где-то ошибка',})

    else:
        form = AddExercisesForm()
        return render(request, 'exercises_add.html', {"form": form,
                                                          "practice": practice})


def exercises_complete(request, p_id, exe_id):
    practice = Practice.objects.get(id=p_id)
    exe = Exercises.objects.get(id=exe_id)
    exe.completed = True
    exe.save()
    return redirect('practice_detail', p_id)


def exercises_incomplete(request, p_id, exe_id,):
    practice = Practice.objects.get(id=p_id)
    exe = Exercises.objects.get(id=exe_id)
    exe.completed = False
    exe.save()
    return redirect('practice_detail', p_id)