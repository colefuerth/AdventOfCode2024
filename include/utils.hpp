#pragma once

#include <string>
#include <vector>
#include <execution>

std::vector<std::string> readFile(const std::string& filename);

/**
 * @brief Generic parallel calculation function using templates and concepts
 * @tparam InputType The type of the input values
 * @tparam OutputType The type of the output values
 * @tparam Func The type of the function to apply
 * @tparam Args The types of the additional arguments to pass to the function
 * @param inputs The input values to process
 * @param func The function to apply to each input value
 * @param args The additional arguments to pass to the function
 * @note The only restriction on the function is that the first argument *must*
 * be the input value of type InputType
 * @return A vector of the calculated output values
 */
template <
    typename InputType, typename OutputType, typename Func, typename... Args>
    requires std::invocable<Func, InputType, Args...> &&
             std::same_as<
                 std::invoke_result_t<Func, InputType, Args...>, OutputType>
static std::vector<OutputType>
map_reduce(const std::vector<InputType> &inputs, Func func, Args... args)
{
    std::vector<OutputType> outputs(inputs.size());
    std::for_each(
        std::execution::par_unseq, inputs.begin(), inputs.end(),
        [&](const InputType &input) {
            size_t index = &input - &inputs[0];
            outputs[index] = func(input, args...);
        }
    );

    return outputs;
}