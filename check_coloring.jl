#!/usr/bin/env -S julia --color=yes --startup-file=no

function read_graph(io)
    header = true
    n = m = 0
    adj_list = Vector{Int}[]
    for line in eachline(io)
        if header
            n, m = parse.(Int, split(line))
            for _ in 1:n
                push!(adj_list, Int[])
            end
            header = false
            continue
        end
        a, b = parse.(Int, split(line))
        push!(adj_list[a], b)
        push!(adj_list[b], a)
    end

    return adj_list
end

function check_coloring(g, c)
    violations = NTuple{3, Int}[]
    for (i, neighbors) in pairs(g)
        for neighbor in neighbors
            neighbor < i && continue
            if c[i] == c[neighbor]
                push!(violations, (i, neighbor, c[i]))
            end
        end
    end

    return violations
end

function read_coloring(io)
    coloring = NTuple{2, Int}[]
    for line in eachline(io)
        i, c = parse.(Int, split(line))
        push!(coloring, (i, c))
    end
    sort!(coloring)
    @assert all(first.(coloring) .== 1:length(coloring))
    return last.(coloring)
end

function main()
    if length(ARGS) != 2
        println("usage: julia check_coloring.jl <graph filename> <coloring filename>")
        exit()
    end

    local g :: Vector{Vector{Int}}
    local c :: Vector{Int}
    open(ARGS[1], "r") do io
        g = read_graph(io)
    end
    open(ARGS[2], "r") do io
        c = read_coloring(io)
    end

    violations = check_coloring(g, c)

    if isempty(violations)
    	qt_colors_used = length(unique(last.(c)))
    	println("Files '$(ARGS[1])' and '$(ARGS[2])' passed the test -- $(qt_colors_used) colors used.")
	if qt_colors_used > 5
		@warn "Um grafo planar não deveria precisar mais que 5 cores usando esse algoritmo."
	end
    else
        println("INVALID COLORING: there are adjacent nodes with same color:")
        for (a, b, c) in violations
            println("Nodes '$a' and '$b' have color '$c'.")
        end
    end
end

main()

