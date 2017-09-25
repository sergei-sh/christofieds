import matplotlib.pyplot
import pylab

y = [0.0026199817657470703, 0.002380847930908203, 0.0030524730682373047, 0.0031211376190185547, 0.005843400955200195, 0.005254030227661133, 0.005739450454711914, 0.0056574344635009766, 0.006348371505737305, 0.009703874588012695, 0.012574195861816406, 0.011842489242553711, 0.015279769897460938, 0.012929677963256836, 0.013797283172607422, 0.023363113403320312, 0.0181429386138916, 0.022124052047729492, 0.022799253463745117, 0.0206148624420166, 0.026204586029052734, 0.022010326385498047, 0.02666759490966797, 0.032819271087646484, 0.031009197235107422, 0.03791952133178711, 0.038437604904174805, 0.04715752601623535, 0.024913787841796875, 0.03356122970581055, 0.02552008628845215, 0.03616690635681152, 0.02997446060180664, 0.030444622039794922, 0.03724527359008789, 0.03389859199523926, 0.043480873107910156, 0.04278111457824707, 0.04027748107910156, 0.0391230583190918, 0.04540848731994629, 0.06565451622009277, 0.05927848815917969, 0.05537915229797363, 0.04999399185180664, 0.05295610427856445, 0.06617927551269531, 0.05540776252746582, 0.05655622482299805, 0.06432318687438965, 0.06985688209533691, 0.054305315017700195, 0.058533430099487305, 0.0738987922668457, 0.07682394981384277, 0.07363462448120117, 0.086675405502319]
x = range(0, len(y))

approx_y = [1.0, 1.0, 1.0000000000000002, 1.0168, 1.1009269997766933, 1.1088914064682205, 1.0580, 1.1082943626228945, 1.0935141358494975, 1.0510]
approx_x = range(2, 12)

plt = matplotlib.pyplot
plt.xlabel("Graph vertex count")
if True:
    plt.scatter(x, y)
    plt.ylabel("Time, s")
else:
    plt.scatter(approx_x, approx_y, marker="^", color="r")
    plt.ylabel("Approximation ratio")
    plt.ylim([0, 1.2])

matplotlib.pyplot.show()
