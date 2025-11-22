"""
Tutu Prompt Master v3.0
Template Manager for GPT-4o Image Prompts (333 Cases)

A simplified prompt template browser with bilingual support.

Author: Tutu API Team
Version: 3.0.0
"""

import os
import sys

try:
    from .template_adapter import PromptTemplateAdapter
except ImportError:
    from template_adapter import PromptTemplateAdapter


class TutuPromptMasterV3:
    """
    Tutu Prompt Master v3.0 - Browse and use 333 GPT-4o prompt templates
    
    Features:
    - 333 high-quality prompt templates across 10 categories
    - Visual template browser with preview
    - Bilingual support (Chinese/English)
    - One-click template loading and combination
    """
    
    def __init__(self):
        """Initialize with template adapter"""
        try:
            self.adapter = PromptTemplateAdapter()
            self.initialized = True
        except Exception as e:
            print(f"[Tutu v3] ERROR: Failed to initialize adapter: {e}")
            self.adapter = None
            self.initialized = False
    
    @classmethod
    def INPUT_TYPES(cls):
        """Define node inputs"""
        return {
            "required": {
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "placeholder": "在此输入您的提示词...\n\n点击下方的「浏览模板」按钮加载模板。",
                    "dynamicPrompts": False
                })
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("final_prompt",)  # 保持英文以兼容工作流
    FUNCTION = "generate_prompt"
    CATEGORY = "Tutu"
    OUTPUT_NODE = False
    
    def generate_prompt(self, prompt=""):
        """
        Generate final prompt
        
        Args:
            prompt: User's prompt text (can be manually edited or loaded from templates)
        
        Returns:
            (final_prompt,)
        """
        # Simply return the prompt as-is
        return (prompt,)


# ======================== Node Registration ========================

NODE_CLASS_MAPPINGS = {
    "TutuPromptMasterV3": TutuPromptMasterV3
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TutuPromptMasterV3": "🎨 Tutu 图图香蕉模型提示词模板管理器"
}

