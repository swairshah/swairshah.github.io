using Plots, Distributions, StatsBase
using Interact, LsqFit
theme(:bright)
gr(
    size = (450, 350),
    leg = false,
    markerstrokewidth = 0,
    markersize = 2,
    bg=colorant"#FFFFF8",
    dpi=300,
    ylims = (-0.3, 1.5),
    xlims = (1, 50)
);

gr(
    leg = false,
    bg=colorant"#FFFFF8"
)

using Plots, Interact
@manipulate for a=1:10, b=0.01:0.01:1, c=1:25
    @. f(x) = a/(1 + ℯ^(-b*x + c))
    x = 1:0.5:50
    plot(x, f(x), size=(200,300), dpi=120)
end

p = [1.0, -0.5, 10]
@. model(x, p) = p[1] / (1 + ℯ^(p[2] * x + p[3]))

x = range(0, step = 0.5, length = 100)
y_real = model(x, p);

#plot(x, y_real)
#scatter!(x, y_obs, m=:X, msize=8, c=:grey, alpha=0.8)

y_obs = y_real + 0.01 * randn(length(x))
p_est = [0.5, -0.3, 5.0]
@time anim = @animate for i = 5:2:100
    fit = curve_fit(model, x[1:i], y_obs[1:i], p_est)
    plot(x, y_real)
    plot!(x, model(x, fit.param))
    scatter!(x[1:i], y_obs[1:i], m=:X,
             alpha=0.8, msize=3, c=:grey)
    vline!([x[i]], c=:grey, style = :dash)
end
gif(anim, "figures/s-model.gif", fps = 5)


using Measurements
y_obs = model(x, p) .± rand(Normal(0, 1), length(x))
@time anim = @animate for i = 5:2:100
    plot(x, y_real)
    fit = curve_fit(model, x[1:i] .± 0, y_obs[1:i], p_est .± 0)
    plot!(x, model(x .± 0, fit.param))
    scatter!(x[1:i], Measurements.value.(y_obs[1:i]), m=:X,
             alpha = 0.8, msize=5, c=:grey)
    vline!([x[i]], c = :grey, style=:dash)
end
gif(anim, "figures/s-model-errors.gif", fps = 5)
